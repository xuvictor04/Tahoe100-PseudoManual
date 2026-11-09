---
symbol: "RPS21"
type: "gene"
col: 10175
ensembl_id: "ENSG00000171858"
name: "ribosomal protein S21"
location: "20q13.33"
module: 131
arm: "+"
pooled_cpm: 244.18
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/131"]
generated_by: "tahoemap"
---

# RPS21

*ribosomal protein S21* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.53× (z +6.7, q 2e-08, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 8.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.430× (z -7.2, q 5e-10, down in 47 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (LS 180 0.202×, NCI-H2030 0.252×, NCI-H460 0.295×, SNU-1 0.267×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.186×); [[Finasteride (drug)]] 5 µM in 1 line (SW 1088 0.0851×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP2]] (+0.97, fdr 7e-06), [[RPS25]] (+0.96, fdr 7e-06), [[RPS10]] (+0.95, fdr 7e-06); moves opposite to [[EIF4G2]] (-0.73, fdr 7e-06), [[PNPO]] (-0.69, fdr 7e-06).
> It is in [[Module 131]], a single-armed module (Eukaryotic Translation Termination).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MIR193BHG]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (COLO 205 8.03×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.53×** | +6.7 | 2e-08 | 48/49 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.57×** | +5.4 | 2e-05 | 43/44 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **2.21×** | +4.8 | 3e-04 | 47/48 (SW 900, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.02×** | +4.2 | 0.003 | 46/48 (NCI-H460, NCI-H1573, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.20×** | +4.2 | 0.003 | 41/45 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (LS 180 0.202×, NCI-H2030 0.252×, NCI-H460 0.295×, SNU-1 0.267×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.186×); [[Finasteride (drug)]] 5 µM in 1 line (SW 1088 0.0851×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.430×** | -7.2 | 5e-10 | 47/48 (LS 180, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -3.6 | 0.095 | 43/48 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 240 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.3) |
| [[BT-474 (line)]] | alt | 92.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.7) |
| [[C-33 A (line)]] | alt | 336 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -9.8) |
| [[COLO 205 (line)]] | alt | 98.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.03× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H2030 (line)]] | alt | 409 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 254 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.1) |
| [[RKO (line)]] | wt | 350 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.9) |
| [[SNU-1 (line)]] | wt | 226 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.0) |
| [[SW 1088 (line)]] | alt | 156 | 0 | 1 | — | [[Finasteride (drug)]] 5 µM 0.0851× (z -8.8) |
| [[SW480 (line)]] | alt | 261 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.0) |
| [[A-172 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 262 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 178 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 271 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 154 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 295 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 508 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 176 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 147 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 310 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 369 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 250 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 375 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 231 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 388 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 273 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 21 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP2]] | +0.97 | +0.94 / +0.97 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS25]] | +0.96 | +0.91 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPS10]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL32]] | +0.94 | +0.89 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL38]] | +0.94 | +0.90 / +0.94 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS29]] | +0.93 | +0.90 / +0.96 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL28]] | +0.93 | +0.89 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS11]] | +0.92 | +0.92 / +0.93 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL36A]] | +0.92 | +0.87 / +0.95 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS23]] | +0.92 | +0.87 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[RPL34]] | +0.92 | +0.88 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS13]] ⚠ | +0.91 | +0.85 / +0.95 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[RPL31]] | +0.90 | +0.84 / +0.93 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.73 | -0.70 / -0.66 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[PNPO]] | -0.69 | -0.67 / -0.70 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR193BHG]] | C | MIR193BHG activity lowers RPS21's level | lines that do not express MIR193BHG (4) vs lines expressing it (46) | 1.54× higher at baseline in the lines without MIR193BHG | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FLVCR2, NINJ1, ZNF845; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 131]] — Eukaryotic Translation Termination; 36 genes; every member is in the + arm (projection on the module's main direction 0.969). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-47.1, -27.0); signed map (-61.5, -3.2). **Vector** length 95.5, 59.8% of its response variance represented; |z| ≥ 3 in 392 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide* (reactome, mean cos +0.91 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.0 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.0 | +0.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.0 | +0.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -6.4 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -6.4 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -6.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.4 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:62,387,103-62,388,520 (+) |
| Ensembl biotype | protein_coding |
| Also known as | S21, eS21 |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P63220](https://www.uniprot.org/uniprotkb/P63220) (Small ribosomal subunit protein eS21):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6227](https://www.ncbi.nlm.nih.gov/gene/6227):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S21E family of ribosomal proteins. It is located in the cytoplasm. Alternative splice variants that encode different protein isoforms have been described, but their …

**Accessions** — [HGNC:10409](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10409) · Entrez [6227](https://www.ncbi.nlm.nih.gov/gene/6227) · UniProt [P63220](https://www.uniprot.org/uniprotkb/P63220) · Ensembl [ENSG00000171858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171858)

## Data

Gene col 10175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10175); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10175]; `tensor/DDL_lfc|DDL_z.npy` [10175]; `embed/gene_vectors.npy` [10175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10175 or target_col == 10175). Every well: [[RPS21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
