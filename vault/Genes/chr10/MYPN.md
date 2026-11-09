---
symbol: "MYPN"
type: "gene"
col: 6157
ensembl_id: "ENSG00000138347"
name: "myopalladin"
location: "10q21.3"
module: 66
arm: "+"
pooled_cpm: 26.3
n_lines_expressing: 21
n_dd_up: 47
n_dd_down: 12
n_dd_up_clean: 36
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# MYPN

*myopalladin* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 47 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.74× (z +15.5, q 0e+00, up in 14 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Betamethasone dipropionate (drug)]] 0.05 µM: 0.580× (z -5.5, q 1e-05, down in 8 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMO]] (+0.67, fdr 1e-05), [[KYNU]] (+0.65, fdr 1e-05), [[NR3C1]] (+0.62, fdr 1e-05); moves opposite to [[FAH]] (-0.54, fdr 2e-05), [[HPCAL1]] (-0.54, fdr 3e-05), [[SHQ1]] (-0.51, fdr 4e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[PLA2G4C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 47 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.74×** | +15.5 | 0e+00 | 14/19 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.98×** | +15.1 | 0e+00 | 15/19 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +14.5 | 1e-45 | 9/17 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.60×** | +12.9 | 4e-36 | 5/16 (MIA PaCa-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +11.0 | 4e-26 | 9/17 (NCI-H1573, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.92×** | +10.0 | 9e-22 | 15/19 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +9.3 | 2e-18 | 2/12 (HOP62, PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.03×** | +7.7 | 9e-13 | 15/19 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +7.4 | 7e-12 | 10/17 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.89×** | +6.7 | 1e-09 | 13/19 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +6.6 | 2e-09 | 6/18 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +6.4 | 7e-09 | 4/18 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.64×** | +6.2 | 2e-08 | 12/19 (NCI-H460, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +6.2 | 3e-08 | 13/19 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.73×** | +5.7 | 4e-07 | 11/18 (NCI-H460, A549, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.65×** | +5.3 | 4e-06 | 11/19 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.40×** | +5.0 | 2e-05 | 8/19 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.9 | 2e-05 | 5/19 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +4.8 | 5e-05 | 6/18 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +4.8 | 5e-05 | 8/17 (BT-474, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.580×** | -5.5 | 1e-05 | 8/18 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.607×** | -5.5 | 1e-05 | 14/19 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.616×** | -5.3 | 2e-05 | 13/19 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.658×** | -4.6 | 6e-04 | 10/19 (Hs 766T, Panc 03.27, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.660×** | -4.6 | 6e-04 | 10/19 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.670×** | -4.4 | 0.001 | 11/19 (Hs 766T, NCI-H460, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.674×** | -4.3 | 0.001 | 9/19 (Hs 766T, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.722×** | -3.6 | 0.025 | 8/19 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.026 | 8/19 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **0.798×** | -3.5 | 0.026 | 8/19 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.733×** | -3.4 | 0.034 | 8/18 (Hs 766T, NCI-H1573, …) | rises with dose |  |
| [[Doxycycline (monohydrate) (drug)]] 5 µM |  | **0.727×** | -3.4 | 0.036 | 2/19 (NCI-H1573, Panc 03.27) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 151 | 7 | 4 (3 ⚠) | [[Trametinib (drug)]] 0.05 µM 2.90× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.0660× (z -19.6) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 161 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.233× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 37.2 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +19.3) | — |
| [[A-427 (line)]] | wt | 297 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.28× (z +10.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -14.2) |
| [[NCI-H1792 (line)]] | alt | 74.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0376× (z -17.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 8.18 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 8.10 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +11.0) | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 1 | — | [[Erlotinib (drug)]] 5 µM 0.0567× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 16.6 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.134× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0815× (z -10.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[PANC-1 (line)]] | alt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.82× (z +9.5) | — |
| [[A-172 (line)]] | wt | 5.73 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.36 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.12 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.97 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.01 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMO]] | +0.67 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[KYNU]] | +0.65 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[NR3C1]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[OLR1]] | +0.62 | +0.49 / +0.59 | both halves | 2e-05 |  |
| [[TRIML2]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[DIO2]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP42]] | +0.61 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[FLRT2]] | +0.61 | +0.59 / +0.36 | both halves | 1e-04 |  |
| [[TNFRSF11B]] | +0.60 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[FGF2]] | +0.60 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[TENM3-AS1]] | +0.60 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[CCDC3]] | +0.60 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAH]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HPCAL1]] | -0.54 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[SHQ1]] | -0.51 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[PHKA2]] | -0.50 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[PACSIN2]] | -0.49 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[EIF4EBP1]] | -0.49 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[RILPL2]] | -0.49 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[PYGB]] | -0.49 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[LPCAT4]] | -0.49 | -0.43 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYPN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[P3H2]] | C | P3H2 activity raises MYPN's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 2.63× lower at baseline in the lines without P3H2 | 0.042 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLA2G4C]] | B | MYPN activity raises PLA2G4C's level | lines that do not express MYPN (29) vs lines expressing it (21) | 1.37× lower at baseline in the lines without MYPN | 0.038 | ⚠ within organs, on part of the lines; also absent: COL4A6, EPGN, FLRT2 |
| [[CYP1B1-AS1]] | B | MYPN activity raises CYP1B1-AS1's level | lines that do not express MYPN (29) vs lines expressing it (21) | 2.02× lower at baseline in the lines without MYPN | 0.067 | ⚠ within organs, on part of the lines; also absent: COL4A6, EPGN, FLRT2 |
| [[PLS3-AS1]] | B | MYPN activity raises PLS3-AS1's level | lines that do not express MYPN (29) vs lines expressing it (21) | 1.52× lower at baseline in the lines without MYPN | 0.084 | ⚠ within organs, on part of the lines; also absent: COL4A6, EPGN, FLRT2 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.8, 22.4); signed map (47.0, 22.5). **Vector** length 77.3, 23.2% of its response variance represented; |z| ≥ 3 in 684 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +12.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +15.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.3 | +6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +5.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.7 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -4.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.3 | -4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.2 | -5.3 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.9 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | myopalladin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:68,087,897-68,212,017 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MYOP |
| Gene groups (HGNC) | I-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86TC9](https://www.uniprot.org/uniprotkb/Q86TC9) (Myopalladin):

> Component of the sarcomere that tethers together nebulin (skeletal muscle) and nebulette (cardiac muscle) to alpha-actinin, at the Z lines.

**Summary**, from NCBI Gene [84665](https://www.ncbi.nlm.nih.gov/gene/84665):

> Striated muscle in vertebrates comprises large proteins which must be organized properly to contract efficiently. Z-lines in striated muscle are a sign of this organization, representing the ends of actin thin filaments, titin, nebulin or nebulette and accessory proteins required for structure and function. This gene encodes a protein which interacts with nebulin in skeletal muscle or nebulette in cardiac muscle and alpha-actinin. In addition, this gene product can interact with a protein with …

**Accessions** — [HGNC:23246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23246) · Entrez [84665](https://www.ncbi.nlm.nih.gov/gene/84665) · UniProt [Q86TC9](https://www.uniprot.org/uniprotkb/Q86TC9) · Ensembl [ENSG00000138347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138347)

## Data

Gene col 6157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6157); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6157]; `tensor/DDL_lfc|DDL_z.npy` [6157]; `embed/gene_vectors.npy` [6157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6157 or target_col == 6157). Every well: [[MYPN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYPN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
