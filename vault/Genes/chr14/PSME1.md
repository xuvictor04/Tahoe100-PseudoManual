---
symbol: "PSME1"
type: "gene"
col: 1683
ensembl_id: "ENSG00000092010"
name: "proteasome activator subunit 1"
location: "14q12"
module: 70
arm: "+"
pooled_cpm: 74.66
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# PSME1

*proteasome activator subunit 1* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.81× (z +7.1, q 5e-10, up in 44 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 3.85×, NCI-H460 3.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.621× (z -5.6, q 9e-06, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.179×, LoVo 0.349×, SW480 0.356×, SW1417 0.427×); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 0.210×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B2M]] (+0.76, fdr 7e-06), [[PSMB9]] (+0.74, fdr 7e-06), [[LY6E]] (+0.73, fdr 7e-06); moves opposite to [[LINC00941]] (-0.56, fdr 2e-05), [[ELK3]] (-0.54, fdr 2e-05), [[DCTD]] (-0.54, fdr 4e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RSAD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1683.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW480 3.85×, NCI-H460 3.87×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.81×** | +7.1 | 5e-10 | 44/49 (C-33 A, HOP62, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.25×** | +6.6 | 1e-08 | 39/42 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.86×** | +5.2 | 3e-05 | 44/48 (SW 900, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +4.7 | 4e-04 | 36/45 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Bendamustine (drug)]] 5 µM |  | 1.47× | +3.1 | 0.20 | 33/48 (SW1417, SNU-423, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.1 | 0.20 | 3/49 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1683.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.179×, LoVo 0.349×, SW480 0.356×, SW1417 0.427×); [[TAK-901 (drug)]] 0.05 µM in 1 line (BT-474 0.210×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.621×** | -5.6 | 9e-06 | 35/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | **0.650×** | -3.6 | 0.084 | 40/48 (AsPC-1, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1683. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 48.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.0) |
| [[A-427 (line)]] | wt | 53.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -15.6) |
| [[BT-474 (line)]] | alt | 117 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.210× (z -9.7) |
| [[LoVo (line)]] | wt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 54.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 91.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -8.9) |
| [[A-172 (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 95.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 88.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 67.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 78.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 72.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1683), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B2M]] | +0.76 | +0.71 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 546 |
| [[PSMB9]] | +0.74 | +0.70 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 993 |
| [[LY6E]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[HLA-B]] | +0.71 | +0.68 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[GBP4]] | +0.70 | +0.69 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFITM3]] | +0.69 | +0.62 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PSME2]] | +0.69 | +0.52 / +0.79 | both halves | 1e-05 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 999; ⚠ same locus (4.4 kb: neighbours can correlate without regulation) |
| [[ISG15]] | +0.67 | +0.55 / +0.76 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[UBE2L6]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM; STRING 755 |
| [[IFI30]] | +0.65 | +0.63 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI6]] | +0.64 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[TNFSF10]] | +0.64 | +0.54 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[HERC5]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00941]] | -0.56 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[ELK3]] | -0.54 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[DCTD]] | -0.54 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[ASB1]] | -0.54 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[MAK16]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[HMGA2]] | -0.51 | -0.46 / -0.43 | both halves | 4e-05 |  |
| [[TRMT6]] | -0.51 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RSAD2]] | B | RSAD2 activity raises PSME1's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.47× lower at baseline in the lines without RSAD2 | 0.004 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[GBP1]] | B | GBP1 activity raises PSME1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without GBP1 | 0.028 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[CD5L]] | B | CD5L activity raises PSME1's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.30× lower at baseline in the lines without CD5L | 0.047 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[IFI27]] | B | IFI27 activity raises PSME1's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.35× lower at baseline in the lines without IFI27 | 0.048 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[MX1]] | B | MX1 activity raises PSME1's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.21× lower at baseline in the lines without MX1 | 0.057 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI44L]] | B | IFI44L activity raises PSME1's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 1.21× lower at baseline in the lines without IFI44L | 0.079 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[TNFSF10]] | B | TNFSF10 activity raises PSME1's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 1.39× lower at baseline in the lines without TNFSF10 | 0.084 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |
| [[SP110]] | B | SP110 activity raises PSME1's level | lines that do not express SP110 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without SP110 | 0.087 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises PSME1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.30× lower at baseline in the lines without GBP4 | 0.090 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[ISG15]] | C | ISG15 activity raises PSME1's level | lines that do not express ISG15 (4) vs lines expressing it (46) | 1.56× lower at baseline in the lines without ISG15 | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: IFIH1, IFI35, NUTM2A-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.5, 50.4); signed map (65.4, 27.9). **Vector** length 73.9, 28.5% of its response variance represented; |z| ≥ 3 in 468 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interferon gamma signaling* (reactome, mean cos +0.59 to 13); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.57 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.57 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +1.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.6 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.1 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -3.9 | +7.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.5 | -1.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | proteasome activator subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,136,163-24,138,967 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IFI5111, PA28alpha |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, FATTY_ACID_METABOLISM, INTERFERON_GAMMA_RESPONSE |
| Reactome | 7 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Cross-presentation of soluble exogenous antigens (endosomes); Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06323](https://www.uniprot.org/uniprotkb/Q06323) (Proteasome activator complex subunit 1):

> Implicated in immunoproteasome assembly and required for efficient antigen processing. The PA28 activator complex enhances the generation of class I binding peptides by altering the cleavage pattern of the proteasome.

**Summary**, from NCBI Gene [5720](https://www.ncbi.nlm.nih.gov/gene/5720):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9568) · Entrez [5720](https://www.ncbi.nlm.nih.gov/gene/5720) · UniProt [Q06323](https://www.uniprot.org/uniprotkb/Q06323) · Ensembl [ENSG00000092010](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092010)

## Data

Gene col 1683: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1683); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1683, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1683]; `tensor/DDL_lfc|DDL_z.npy` [1683]; `embed/gene_vectors.npy` [1683]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1683 or target_col == 1683). Every well: [[PSME1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSME1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
