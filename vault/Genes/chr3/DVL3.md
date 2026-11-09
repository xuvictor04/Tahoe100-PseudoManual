---
symbol: "DVL3"
type: "gene"
col: 8419
ensembl_id: "ENSG00000161202"
name: "dishevelled segment polarity protein 3"
location: "3q27.1"
module: 126
arm: "+"
pooled_cpm: 40.14
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 6
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# DVL3

*dishevelled segment polarity protein 3* — 3q27.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.92× (z +15.6, q 0e+00, up in 41 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.48× (z +9.4, q 9e-19, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.615× (z -11.6, q 3e-28, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATN1]] (+0.70, fdr 3e-05), [[INPPL1]] (+0.67, fdr 1e-05), [[CERS2]] (+0.66, fdr 5e-05); moves opposite to [[MRPL14]] (-0.60, fdr 2e-04), [[UGCG]] (-0.59, fdr 2e-05), [[CFD]] (-0.58, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8419.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +15.6 | 0e+00 | 41/45 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +15.1 | 0e+00 | 32/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +10.4 | 7e-23 | 30/43 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.48×** | +9.4 | 9e-19 | 35/48 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +7.6 | 3e-12 | 32/48 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +7.4 | 1e-11 | 32/48 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +7.1 | 1e-10 | 29/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +7.0 | 2e-10 | 25/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +6.8 | 5e-10 | 30/46 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.15× | +4.7 | 2e-04 | 13/48 (J82, A498, …) | top dose only | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 16/47 (NCI-H460, H4, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 0.05 µM |  | 1.19× | +3.9 | 0.004 | 13/48 (NCI-H2030, SW480, …) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.12× | +3.7 | 0.010 | 13/48 (SW1417, KATO III, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.012 | 16/48 (J82, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.16× | +3.4 | 0.026 | 10/47 (NCI-H23, SNU-423, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.026 | 11/48 (BT-474, SW480, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +3.3 | 0.028 | 9/47 (NCI-H1573, NCI-H2030, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.039 | 3/48 (A498, SNU-423, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8419.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.615×** | -11.6 | 3e-28 | 38/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.871× | -11.1 | 5e-26 | 11/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.737×** | -10.2 | 5e-22 | 40/48 (SW480, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.658×** | -10.0 | 2e-21 | 39/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.743×** | -7.1 | 1e-10 | 28/48 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.817×** | -4.8 | 1e-04 | 20/48 (CHP-212, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.865× | -4.6 | 3e-04 | 9/48 (LoVo, HT-29, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.835× | -4.3 | 0.001 | 13/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.712×** | -4.2 | 0.001 | 19/49 (CFPAC-1, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 0.5 µM |  | 0.861× | -3.6 | 0.022 | 14/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8419. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 44.5 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +11.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.451× (z -11.2) |
| [[KATO III (line)]] | alt | 45.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.370× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 25.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.71× (z +8.6) | — |
| [[J82 (line)]] | alt | 52.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.0) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 41.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.34× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 58.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 47.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 52.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.4) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 55.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 41.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 48.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 61.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 82.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8419), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATN1]] | +0.70 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[INPPL1]] | +0.67 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CERS2]] | +0.66 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[KMT2D]] | +0.65 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[STX16]] | +0.63 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[TOR1A]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[LDB1]] | +0.60 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[PLPBP]] | +0.60 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[EXOC7]] | +0.59 | +0.40 / +0.62 | both halves | 4e-05 |  |
| [[UNC50]] | +0.59 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[MFN2]] | +0.59 | +0.40 / +0.61 | both halves | 4e-05 |  |
| [[MCM3AP]] | +0.59 | +0.46 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL14]] | -0.60 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[UGCG]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[CFD]] | -0.58 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[RPL22L1]] ⚠ | -0.57 | -0.19 / -0.66 | ⚠ one half (not replicated) | 8e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS26]] | -0.57 | -0.24 / -0.58 | both halves | 5e-04 |  |
| [[ATP5F1D]] ⚠ | -0.57 | -0.13 / -0.59 | ⚠ one half (not replicated) | 0.002 | ⚠ in the vector space only through flagged drug-doses |
| [[CCDC85B]] | -0.56 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[PPP2R2A]] | -0.56 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[ANTKMT]] | -0.55 | -0.14 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[FAM133B]] | -0.55 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[NEDD9]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[GCHFR]] | -0.55 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[LAGE3]] | -0.54 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[ANAPC11]] | -0.54 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[IMP3]] | -0.53 | -0.35 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DVL3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DVL3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers DVL3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.6, -22.6); signed map (-11.5, -35.1). **Vector** length 98.5, 21.4% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +15.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +15.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.2 | +7.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +7.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +7.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.6 | +1.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -10.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.4 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.7 | -7.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Allantoin (drug)]] 0.5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | dishevelled segment polarity protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.1 — chr3:184,155,377-184,173,614 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0208 |
| Gene groups (HGNC) | Dishevelled segment polarity proteins; PDZ domain containing; DEP domain containing |
| Reactome | 17 pathways, smallest: Negative regulation of TCF-dependent signaling by DVL-interacting proteins; WNT mediated activation of DVL; Killing mechanisms |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92997](https://www.uniprot.org/uniprotkb/Q92997) (Segment polarity protein dishevelled homolog DVL-3):

> Involved in the signal transduction pathway mediated by multiple Wnt genes.

**Summary**, from NCBI Gene [1857](https://www.ncbi.nlm.nih.gov/gene/1857):

> This gene is a member of a multi-gene family which shares strong similarity with the Drosophila dishevelled gene, dsh. The Drosophila dishevelled gene encodes a cytoplasmic phosphoprotein that regulates cell proliferation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3087) · Entrez [1857](https://www.ncbi.nlm.nih.gov/gene/1857) · UniProt [Q92997](https://www.uniprot.org/uniprotkb/Q92997) · Ensembl [ENSG00000161202](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161202)

## Data

Gene col 8419: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8419); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8419, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8419]; `tensor/DDL_lfc|DDL_z.npy` [8419]; `embed/gene_vectors.npy` [8419]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8419 or target_col == 8419). Every well: [[DVL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DVL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
