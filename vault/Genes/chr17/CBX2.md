---
symbol: "CBX2"
type: "gene"
col: 10439
ensembl_id: "ENSG00000173894"
name: "chromobox 2"
location: "17q25.3"
module: 176
arm: "+"
pooled_cpm: 5.06
n_lines_expressing: 44
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 11
tags: ["gene", "module/176"]
generated_by: "tahoemap"
---

# CBX2

*chromobox 2* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.52× (z +15.1, q 0e+00, up in 36 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.597× (z -8.9, q 5e-16, down in 20 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAZ]] (+0.66, fdr 1e-05), [[DNMT3B]] (+0.64, fdr 1e-05), [[TBC1D24]] (+0.63, fdr 1e-04); moves opposite to [[PPP1R12A-AS2]] (-0.63, fdr 3e-04), [[METTL6]] (-0.62, fdr 3e-05), [[EYS]] (-0.59, fdr 2e-04).
> It is in [[Module 176]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CELSR2]] → it (grade B ⚠); 11 go from it, the strongest it → [[PSMD14-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10439.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.52×** | +15.1 | 0e+00 | 36/40 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.81×** | +12.4 | 8e-33 | 33/39 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.40×** | +10.5 | 2e-23 | 31/40 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +7.5 | 1e-11 | 17/40 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.85×** | +7.3 | 3e-11 | 12/26 (SW480, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +7.1 | 2e-10 | 19/40 (PANC-1, HT-29, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +5.3 | 1e-05 | 5/34 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.46×** | +4.5 | 4e-04 | 3/21 (LOX-IMVI, A549, …) | all doses, flat | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.5 | 5e-04 | 3/41 (KATO III, LoVo, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.006 | 5/32 (NCI-H2030, A-172, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.34×** | +3.4 | 0.039 | 8/23 (SW480, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.32×** | +3.3 | 0.043 | 7/40 (KATO III, SW480, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.46×** | +3.2 | 0.054 | 2/30 (J82, HOP62) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +3.2 | 0.054 | 4/39 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Apalutamide (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.087 | 3/37 (KATO III, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 1.20× | +3.0 | 0.090 | 4/40 (PANC-1, SK-MEL-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10439.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.597×** | -8.9 | 5e-16 | 20/35 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -6.5 | 3e-08 | 16/31 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -5.2 | 4e-05 | 15/38 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.743×** | -5.1 | 4e-05 | 19/40 (HT-29, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.666×** | -5.0 | 8e-05 | 16/40 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.692×** | -4.3 | 0.001 | 14/38 (J82, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.729×** | -3.9 | 0.008 | 15/40 (HepG2/C3A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.801×** | -3.9 | 0.008 | 11/34 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **0.827×** | -3.3 | 0.057 | 14/40 (SHP-77, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.763×** | -3.1 | 0.099 | 10/36 (HepG2/C3A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10439. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 6.93 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.127× (z -8.8) |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -9.3) |
| [[LoVo (line)]] | wt | 6.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0737× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 6.70 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0693× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 5.78 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0945× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 5.16 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0448× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -12.9) |
| [[SW48 (line)]] | wt | 10.3 | 0 | 1 | — | [[Mozavaptan (drug)]] 5 µM 0.0724× (z -8.5) |
| [[A-172 (line)]] | wt | 6.31 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.624 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10439), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAZ]] | +0.66 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[DNMT3B]] | +0.64 | +0.49 / +0.56 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[TBC1D24]] | +0.63 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[CASP2]] | +0.62 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[PODXL2]] | +0.60 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[TMEM201]] | +0.60 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[AIF1L]] | +0.60 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[GLB1L2]] | +0.60 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[RADIL]] | +0.59 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[LRRC20]] | +0.59 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[CEP72]] | +0.59 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[C20orf27]] | +0.59 | +0.54 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12A-AS2]] | -0.63 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[METTL6]] | -0.62 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[EYS]] | -0.59 | -0.43 / -0.32 | both halves | 2e-04 |  |
| [[AP4S1]] | -0.59 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ATE1OSP]] | -0.59 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[AIMP1]] | -0.59 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[GTF2IRD2]] | -0.59 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[PKN2-AS1]] | -0.59 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[USP34-DT]] | -0.59 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[LINC02951]] | -0.58 | -0.49 / -0.27 | both halves | 3e-04 |  |
| [[CCDC122]] | -0.58 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[MFF-DT]] | -0.58 | -0.47 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR2]] | B | CELSR2 activity raises CBX2's level | lines that do not express CELSR2 (9) vs lines expressing it (41) | 2.21× lower at baseline in the lines without CELSR2 | 0.037 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, CMTM8; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises CBX2's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without SEPTIN3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMD14-DT]] | B | CBX2 activity raises PSMD14-DT's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.35× lower at baseline in the lines without CBX2 | 0.001 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[TMEM201]] | B | CBX2 activity raises TMEM201's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without CBX2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[TBC1D24]] | B | CBX2 activity raises TBC1D24's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.73× lower at baseline in the lines without CBX2 | 0.034 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[RFX3-DT]] | B | CBX2 activity raises RFX3-DT's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 2.31× lower at baseline in the lines without CBX2 | 0.035 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[SMIM19]] | B | CBX2 activity raises SMIM19's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without CBX2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[RNFT2]] | B | CBX2 activity raises RNFT2's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 2.69× lower at baseline in the lines without CBX2 | 0.040 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[TBCE-1]] | B | CBX2 activity raises TBCE-1's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without CBX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[GNAZ]] | B | CBX2 activity raises GNAZ's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 2.89× lower at baseline in the lines without CBX2 | 0.065 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[ACTR3-AS1]] | B | CBX2 activity raises ACTR3-AS1's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without CBX2 | 0.085 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[C15orf39]] | B | CBX2 activity lowers C15orf39's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.56× higher at baseline in the lines without CBX2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |
| [[TMEM170B]] | B | CBX2 activity raises TMEM170B's level | lines that do not express CBX2 (6) vs lines expressing it (44) | 1.85× lower at baseline in the lines without CBX2 | 0.095 | ⚠ within organs, on part of the lines; also absent: CCNP, CTXN1, ADGRL1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 176]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.656). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.7, 5.9); signed map (-40.4, -7.2). **Vector** length 54.2, 7.43% of its response variance represented; |z| ≥ 3 in 1,007 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +15.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +12.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.8 | +10.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +7.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +0.8 | +1.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -8.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.2 | -6.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -4.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -0.8 | +0.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | chromobox 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:79,778,148-79,787,983 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10561, M33; previously CDCA6 |
| Gene groups (HGNC) | Chromobox family |
| Reactome | 19 pathways, smallest: SUMOylation of DNA methylation proteins; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; SUMOylation of transcription cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14781](https://www.uniprot.org/uniprotkb/Q14781) (Chromobox protein homolog 2):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. Binds to histone H3 trimethylated at 'Lys-9' (H3K9me3) or at 'Lys-27' (H3K27me3) (By similarity). …

**Summary**, from NCBI Gene [84733](https://www.ncbi.nlm.nih.gov/gene/84733):

> This gene encodes a component of the polycomb multiprotein complex, which is required to maintain the transcriptionally repressive state of many genes throughout development via chromatin remodeling and modification of histones. Disruption of this gene in mice results in male-to-female gonadal sex reversal. Mutations in this gene are also associated with gonadal dysgenesis in humans. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by …

**Accessions** — [HGNC:1552](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1552) · Entrez [84733](https://www.ncbi.nlm.nih.gov/gene/84733) · UniProt [Q14781](https://www.uniprot.org/uniprotkb/Q14781) · Ensembl [ENSG00000173894](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173894)

## Data

Gene col 10439: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10439); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10439, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10439]; `tensor/DDL_lfc|DDL_z.npy` [10439]; `embed/gene_vectors.npy` [10439]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10439 or target_col == 10439). Every well: [[CBX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
