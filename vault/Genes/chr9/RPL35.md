---
symbol: "RPL35"
type: "gene"
col: 5947
ensembl_id: "ENSG00000136942"
name: "ribosomal protein L35"
location: "9q33.3"
module: 43
arm: "+"
pooled_cpm: 203.2
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/043", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# RPL35

*ribosomal protein L35* — 9q33.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.86× (z +7.4, q 1e-10, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.308×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS17]] (+0.96, fdr 7e-06, ⚠ RPS17 in the vector space only through flagged drug-doses), [[RPL26]] (+0.96, fdr 7e-06), [[RPL23]] (+0.95, fdr 7e-06), [[RPL35A]] (+0.95, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[MZT2A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 8 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **3.86×** | +7.4 | 1e-10 | 48/49 (SW 900, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.99×** | +6.2 | 2e-07 | 42/44 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.8 | 4e-04 | 47/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.34×** | +4.6 | 5e-04 | 42/45 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **2.15×** | +4.5 | 7e-04 | 45/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | 1.74× | +3.3 | 0.10 | 41/48 (NCI-H460, COLO 205, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | 1.74× | +3.2 | 0.12 | 39/47 (SHP-77, COLO 205, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.70× | +3.1 | 0.12 | 41/48 (COLO 205, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5947.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.308×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.638× | -3.7 | 0.12 | 39/48 (C-33 A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 200 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.0) |
| [[A-172 (line)]] | wt | 171 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 134 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 255 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 212 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 186 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 165 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 294 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 161 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 205 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 149 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 176 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 232 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 282 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 248 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 214 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 211 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 250 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 254 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 429 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 284 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 249 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS17]] ⚠ | +0.96 | +0.92 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL26]] | +0.96 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL23]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL35A]] | +0.95 | +0.89 / +0.97 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS14]] | +0.95 | +0.91 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL31]] | +0.95 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL27]] | +0.94 | +0.91 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL9]] ⚠ | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL13]] | +0.94 | +0.91 / +0.93 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL36]] | +0.94 | +0.88 / +0.96 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL17]] | +0.94 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3]] ⚠ | +0.94 | +0.87 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | +0.93 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL19]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS27]] | +0.93 | +0.87 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MZT2A]] | C | RPL35's natural level strengthens MZT2A's drug response | RPL35's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.34; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.944). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-45.4, -27.2); signed map (-60.0, -4.0). **Vector** length 77.9, 53.5% of its response variance represented; |z| ≥ 3 in 451 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *SARS-CoV-1 modulates host translation machinery* (reactome, mean cos +0.79 to 19); *Translation initiation complex formation* (reactome, mean cos +0.75 to 21); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.75 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.0 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -0.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -6.5 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -6.0 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -5.8 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | +0.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | +0.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.6 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L35 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:124,857,880-124,861,981 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L35, uL29 |
| Gene groups (HGNC) | L ribosomal proteins |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P42766](https://www.uniprot.org/uniprotkb/P42766) (Large ribosomal subunit protein uL29):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [11224](https://www.ncbi.nlm.nih.gov/gene/11224):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L29P family of ribosomal proteins. It is located in the cytoplasm. As is typical for genes encoding ribosomal proteins, there are multiple processed pseudogenes of this …

**Accessions** — [HGNC:10344](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10344) · Entrez [11224](https://www.ncbi.nlm.nih.gov/gene/11224) · UniProt [P42766](https://www.uniprot.org/uniprotkb/P42766) · Ensembl [ENSG00000136942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136942)

## Data

Gene col 5947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5947); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5947]; `tensor/DDL_lfc|DDL_z.npy` [5947]; `embed/gene_vectors.npy` [5947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5947 or target_col == 5947). Every well: [[RPL35 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL35.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
