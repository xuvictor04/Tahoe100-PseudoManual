---
symbol: "CXCL16"
type: "gene"
col: 8462
ensembl_id: "ENSG00000161921"
name: "C-X-C motif chemokine ligand 16"
location: "17p13.2"
module: 70
arm: "+"
pooled_cpm: 8.61
n_lines_expressing: 43
n_dd_up: 11
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# CXCL16

*C-X-C motif chemokine ligand 16* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +10.1, q 3e-21, up in 20 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.27× (z +4.1, q 0.004, up in 11 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.621× (z -5.7, q 9e-06, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAP1]] (+0.59, fdr 1e-05), [[CTSS]] (+0.59, fdr 5e-05), [[HLA-C]] (+0.58, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EPCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.27×** | +10.1 | 3e-21 | 20/26 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.34×** | +10.0 | 3e-21 | 9/14 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +7.1 | 3e-10 | 20/33 (KATO III, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.53×** | +4.8 | 3e-04 | 8/19 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +4.2 | 0.003 | 9/18 (A-172, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.004 | 11/39 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.7 | 0.015 | 11/29 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.039 | 5/38 (NCI-H2030, SNU-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.062 | 5/39 (AsPC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.062 | 7/39 (AsPC-1, KATO III, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.075 | 7/39 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.1 | 0.099 | 9/36 (AsPC-1, NCI-H23, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.621×** | -5.7 | 9e-06 | 21/37 (HepG2/C3A, NCI-H2030, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.647×** | -5.4 | 2e-05 | 22/38 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.471×** | -4.9 | 2e-04 | 18/39 (HT-29, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -4.3 | 0.002 | 20/39 (RKO, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -4.2 | 0.003 | 16/39 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.714×** | -4.1 | 0.003 | 13/34 (HS-578T, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.716×** | -4.1 | 0.003 | 12/39 (COLO 205, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.792×** | -4.1 | 0.003 | 20/36 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.734×** | -3.6 | 0.020 | 13/37 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.756×** | -3.5 | 0.029 | 6/39 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.756×** | -3.4 | 0.029 | 19/38 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.602×** | -3.3 | 0.050 | 9/37 (KATO III, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.610×** | -3.2 | 0.062 | 8/35 (NCI-H460, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.776×** | -3.1 | 0.070 | 10/39 (AN3 CA, HCT15, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.778×** | -3.1 | 0.071 | 14/39 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.13 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0608× (z -13.2) |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.164× (z -9.5) |
| [[LoVo (line)]] | wt | 19.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +11.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.275× (z -9.3) |
| [[A498 (line)]] | wt | 3.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0800× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 6.02 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0633× (z -9.8) |
| [[HS-578T (line)]] | alt | 3.60 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0505× (z -9.6) |
| [[KATO III (line)]] | alt | 40.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.278× (z -10.0) |
| [[LS 180 (line)]] | wt | 33.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 9.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 4.14 | 0 | 1 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0581× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 5.69 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 17.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +10.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 1 | — | [[Allantoin (drug)]] 0.5 µM 0.0834× (z -8.6) |
| [[SW480 (line)]] | alt | 5.61 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.758 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAP1]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CTSS]] | +0.59 | +0.40 / +0.58 | both halves | 5e-05 | STRING 557 |
| [[HLA-C]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ADAR]] | +0.58 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[IFI30]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[RNF213]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[GBP1]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TAPBP]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[MYD88]] | +0.55 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[APOBEC3B]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[GBP4]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[HLA-H]] | +0.54 | +0.48 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPCAM]] | B | EPCAM activity raises CXCL16's level | lines that do not express EPCAM (28) vs lines expressing it (22) | 2.38× lower at baseline in the lines without EPCAM | 0.039 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[PLBD1]] | B | PLBD1 activity raises CXCL16's level | lines that do not express PLBD1 (24) vs lines expressing it (26) | 1.90× lower at baseline in the lines without PLBD1 | 0.058 | ⚠ within organs, on part of the lines; also absent: PLBD1-AS1, LINC01357, IKZF3 |
| [[ATP2C2]] | B | ATP2C2 activity raises CXCL16's level | lines that do not express ATP2C2 (32) vs lines expressing it (18) | 2.25× lower at baseline in the lines without ATP2C2 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, GRHL2, ST14 |
| [[OAS1]] | B | OAS1 activity raises CXCL16's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without OAS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[USP18]] | C | USP18 activity raises CXCL16's level | lines that do not express USP18 (4) vs lines expressing it (46) | 2.12× lower at baseline in the lines without USP18 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000280007, OAS3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (47.6, 49.4); signed map (62.9, 27.5). **Vector** length 65.3, 11.9% of its response variance represented; |z| ≥ 3 in 749 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antigen processing-Cross presentation* (reactome, mean cos +0.50 to 14); *Endosomal/Vacuolar pathway* (reactome, mean cos +0.51 to 8); *Antigen Presentation: Folding, assembly and peptide loading of class I MHC* (reactome, mean cos +0.52 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.4 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.0 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +3.0 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -5.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.0 | -3.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | C-X-C motif chemokine ligand 16 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,733,533-4,739,928 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SR-PSOX, CXCLG16, SRPSOX |
| Gene groups (HGNC) | Chemokine ligands; Scavenger receptors |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 7 pathways, smallest: Chemokine receptors bind chemokines; Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2A7](https://www.uniprot.org/uniprotkb/Q9H2A7) (C-X-C motif chemokine 16):

> Acts as a scavenger receptor on macrophages, which specifically binds to OxLDL (oxidized low density lipoprotein), suggesting that it may be involved in pathophysiology such as atherogenesis (By similarity). Induces a strong chemotactic response. Induces calcium mobilization. Binds to CXCR6/Bonzo.

**Summary**, from NCBI Gene [58191](https://www.ncbi.nlm.nih.gov/gene/58191):

> Enables chemokine activity. Involved in several processes, including positive regulation of cell growth; response to tumor necrosis factor; and response to type II interferon. Located in obsolete extracellular space. Biomarker of COVID-19 and systemic scleroderma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16642) · Entrez [58191](https://www.ncbi.nlm.nih.gov/gene/58191) · UniProt [Q9H2A7](https://www.uniprot.org/uniprotkb/Q9H2A7) · Ensembl [ENSG00000161921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161921)

## Data

Gene col 8462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8462); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8462]; `tensor/DDL_lfc|DDL_z.npy` [8462]; `embed/gene_vectors.npy` [8462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8462 or target_col == 8462). Every well: [[CXCL16 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXCL16.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
