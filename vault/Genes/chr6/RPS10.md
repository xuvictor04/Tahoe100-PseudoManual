---
symbol: "RPS10"
type: "gene"
col: 4553
ensembl_id: "ENSG00000124614"
name: "ribosomal protein S10"
location: "6p21.31"
module: 131
arm: "+"
pooled_cpm: 157.73
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPS10

*ribosomal protein S10* — 6p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.04× (z +6.6, q 2e-08, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.42×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.608× (z -4.2, q 0.018, down in 39 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.318×, C-33 A 0.318×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS21]] (+0.95, fdr 7e-06), [[RPL32]] (+0.95, fdr 7e-06), [[RPL36A]] (+0.95, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.70, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MIR193BHG]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4553.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.42×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **3.04×** | +6.6 | 2e-08 | 48/49 (NCI-H460, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.16×** | +4.4 | 0.003 | 38/44 (Hs 766T, NCI-H460, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.22×** | +3.9 | 0.017 | 40/45 (Panc 03.27, KATO III, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.90×** | +3.8 | 0.017 | 42/48 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.81×** | +3.6 | 0.042 | 43/48 (COLO 205, NCI-H1573, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.3 | 0.097 | 39/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4553.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H23 0.318×, C-33 A 0.318×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.608×** | -4.2 | 0.018 | 39/48 (NCI-H23, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 177 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 296 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 75.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 80.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 244 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 81.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 191 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 206 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 110 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 134 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 184 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 114 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 151 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 208 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 212 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 222 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 229 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 175 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 24 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS21]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL32]] | +0.95 | +0.94 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36A]] | +0.95 | +0.91 / +0.96 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 987 |
| [[RPLP2]] | +0.94 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 996 |
| [[RPL38]] | +0.94 | +0.94 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS29]] | +0.94 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS13]] ⚠ | +0.93 | +0.91 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.93 | +0.84 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS16]] ⚠ | +0.93 | +0.86 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL27]] | +0.93 | +0.87 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL34]] | +0.93 | +0.87 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[RPS23]] | +0.93 | +0.91 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL13]] | +0.92 | +0.85 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.70 | -0.62 / -0.65 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR193BHG]] | C | MIR193BHG activity lowers RPS10's level | lines that do not express MIR193BHG (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without MIR193BHG | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FLVCR2, NINJ1, ZNF845; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.961). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-46.7, -27.2); signed map (-61.3, -3.4). **Vector** length 83.0, 50.6% of its response variance represented; |z| ≥ 3 in 365 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.93 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | -0.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.5 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -6.7 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.6 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -6.2 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -0.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | +0.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.31 — chr6:34,417,454-34,426,069 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC88819, S10, eS10 |
| Gene groups (HGNC) | S ribosomal proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P46783](https://www.uniprot.org/uniprotkb/P46783) (Small ribosomal subunit protein eS10):

> Component of the 40S ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6204](https://www.ncbi.nlm.nih.gov/gene/6204):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S10E family of ribosomal proteins. It is located in the cytoplasm. Variable expression of this gene in colorectal cancers compared to adjacent normal tissues has been …

**Accessions** — [HGNC:10383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10383) · Entrez [6204](https://www.ncbi.nlm.nih.gov/gene/6204) · UniProt [P46783](https://www.uniprot.org/uniprotkb/P46783) · Ensembl [ENSG00000124614](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124614)

## Data

Gene col 4553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4553); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4553]; `tensor/DDL_lfc|DDL_z.npy` [4553]; `embed/gene_vectors.npy` [4553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4553 or target_col == 4553). Every well: [[RPS10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
