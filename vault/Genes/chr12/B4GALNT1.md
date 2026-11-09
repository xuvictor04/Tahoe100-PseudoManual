---
symbol: "B4GALNT1"
type: "gene"
col: 5708
ensembl_id: "ENSG00000135454"
name: "beta-1,4-N-acetyl-galactosaminyltransferase 1"
location: "12q13.3"
module: 60
arm: "+"
pooled_cpm: 6.87
n_lines_expressing: 34
n_dd_up: 21
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 11
direction_downstream: 13
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# B4GALNT1

*beta-1,4-N-acetyl-galactosaminyltransferase 1* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.26× (z +12.0, q 2e-30, up in 9 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.98× (z +11.5, q 3e-28, up in 23 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.320× (z -17.0, q 0e+00, down in 26 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINH1]] (+0.68, fdr 1e-05), [[MLLT11]] (+0.68, fdr 7e-06), [[AHSA1]] (+0.67, fdr 1e-05); moves opposite to [[GCAT]] (-0.54, fdr 3e-05), [[TXNIP]] (-0.51, fdr 1e-04), [[SPG11]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 13 go from it, the strongest it → [[SFXN5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.26×** | +12.0 | 2e-30 | 9/10 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.98×** | +11.5 | 3e-28 | 23/30 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.00×** | +10.9 | 1e-25 | 21/28 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.74×** | +10.6 | 3e-24 | 22/31 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +9.4 | 5e-19 | 18/29 (NCI-H1792, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.23×** | +8.5 | 3e-15 | 11/18 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.22×** | +7.8 | 6e-13 | 9/11 (NCI-H1792, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +6.3 | 2e-08 | 20/31 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.8 | 5e-07 | 14/32 (NCI-H1792, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.0 | 3e-05 | 10/20 (NCI-H2030, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.58×** | +4.7 | 2e-04 | 12/26 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.5 | 3e-04 | 11/32 (SW480, NCI-H1792, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +4.1 | 0.002 | 2/14 (PANC-1, HS-578T) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.71×** | +4.0 | 0.002 | 5/30 (NCI-H1792, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.003 | 9/30 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.042 | 7/31 (A-172, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5708.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.320×** | -17.0 | 0e+00 | 26/27 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.357×** | -10.9 | 4e-25 | 21/27 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.460×** | -7.9 | 7e-13 | 21/30 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.520×** | -6.9 | 7e-10 | 15/31 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -6.4 | 2e-08 | 17/28 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.561×** | -6.1 | 1e-07 | 18/31 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -6.0 | 2e-07 | 17/30 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.574×** | -5.9 | 3e-07 | 16/30 (H4, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.602×** | -5.4 | 5e-06 | 18/30 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.867× | -5.2 | 1e-05 | 11/32 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.670×** | -4.2 | 0.001 | 7/31 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.674×** | -4.2 | 0.001 | 13/30 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.685×** | -3.8 | 0.006 | 17/28 (NCI-H2030, AN3 CA, …) | rises with dose | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.748×** | -3.1 | 0.087 | 3/30 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 30.2 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -18.0) |
| [[NCI-H1792 (line)]] | alt | 19.0 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 8.60 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.3) |
| [[A-427 (line)]] | wt | 38.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -17.8) |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0346× (z -17.5) |
| [[NCI-H2030 (line)]] | alt | 15.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 14.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 9.92 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -9.4) |
| [[A498 (line)]] | wt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +10.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0618× (z -9.1) |
| [[HOP62 (line)]] | alt | 4.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -8.5) |
| [[LoVo (line)]] | wt | 4.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0638× (z -12.0) |
| [[SW480 (line)]] | alt | 2.91 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.02× (z +8.6) | — |
| [[A549 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.582 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.984 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.724 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.567 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINH1]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[MLLT11]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.67 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PSMB2]] | +0.65 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[HSP90AA2P]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[NECAB3]] | +0.63 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[USP5]] | +0.60 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[ATP2C1]] | +0.60 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[CNPY4]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[C1orf216]] | +0.59 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[BABAM1]] | +0.58 | +0.64 / +0.36 | both halves | 1e-04 |  |
| [[PSMA1]] | +0.58 | +0.64 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCAT]] | -0.54 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[TXNIP]] | -0.51 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[SPG11]] | -0.50 | -0.54 / -0.33 | both halves | 1e-04 | STRING 447 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers B4GALNT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TXNIP]] | B | TXNIP activity lowers B4GALNT1's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 3.00× higher at baseline in the lines without TXNIP | 0.021 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[KRT16]] | B | KRT16 activity lowers B4GALNT1's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 2.05× higher at baseline in the lines without KRT16 | 0.039 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[XIST]] | B | XIST activity lowers B4GALNT1's level | lines that do not express XIST (43) vs lines expressing it (7) | 1.74× higher at baseline in the lines without XIST | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, GPR15, KRT20 |
| [[ARHGEF25]] | C | ARHGEF25 activity raises B4GALNT1's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 3.76× lower at baseline in the lines without ARHGEF25 | 0.002 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |
| [[MAP1B]] | C | MAP1B activity raises B4GALNT1's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 3.14× lower at baseline in the lines without MAP1B | 0.036 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[ADAM23]] | C | ADAM23 activity raises B4GALNT1's level | lines that do not express ADAM23 (26) vs lines expressing it (24) | 3.43× lower at baseline in the lines without ADAM23 | 0.057 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, GALNT13, CNRIP1; co-absent with the target |
| [[PRAME]] | C | PRAME activity raises B4GALNT1's level | lines that do not express PRAME (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without PRAME | 0.076 | ⚠ within organs, on part of the lines; also absent: GLDC, NR0B1, PAX2; co-absent with the target |
| [[MAP1A]] | C | MAP1A activity raises B4GALNT1's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 2.48× lower at baseline in the lines without MAP1A | 0.087 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[HHIPL2]] | C | HHIPL2 activity raises B4GALNT1's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 3.53× lower at baseline in the lines without HHIPL2 | 0.095 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent; co-absent with the target |
| [[SEPTIN5]] | C | SEPTIN5 activity raises B4GALNT1's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 2.81× lower at baseline in the lines without SEPTIN5 | 0.099 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SFXN5]] | B | B4GALNT1 activity raises SFXN5's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without B4GALNT1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[SMO]] | B | B4GALNT1 activity raises SMO's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 2.88× lower at baseline in the lines without B4GALNT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[CNPY4]] | B | B4GALNT1 activity raises CNPY4's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without B4GALNT1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[HSPA1B]] | B | B4GALNT1 activity lowers HSPA1B's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.50× higher at baseline in the lines without B4GALNT1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[PHTF1]] | B | B4GALNT1 activity raises PHTF1's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without B4GALNT1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[USP5]] | B | B4GALNT1 activity raises USP5's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without B4GALNT1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1 |
| [[KLHL25]] | B | B4GALNT1 activity weakens KLHL25's drug response | lines that do not express B4GALNT1 (16) vs lines expressing it (32) | the lines without B4GALNT1 respond 1.34× as strongly (z diff -0.95); strongest at Ixazomib citrate 5 µM: 3.53x vs 1.91x (z diff -2.6) | 0.094 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; target measured in part of the lines; artifact flags |
| [[ARHGEF25]] | C | B4GALNT1 activity raises ARHGEF25's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without B4GALNT1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; co-absent with the target |
| [[PCOLCE2]] | C | B4GALNT1 activity raises PCOLCE2's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 3.61× lower at baseline in the lines without B4GALNT1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; co-absent with the target |
| [[ADAM23]] | C | B4GALNT1 activity raises ADAM23's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 5.10× lower at baseline in the lines without B4GALNT1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; co-absent with the target |
| [[MLLT11]] | C | B4GALNT1 activity raises MLLT11's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 3.46× lower at baseline in the lines without B4GALNT1 | 0.038 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; co-absent with the target |
| [[SEPTIN5]] | C | B4GALNT1 activity raises SEPTIN5's level | lines that do not express B4GALNT1 (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without B4GALNT1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ARHGEF25, RFLNB, RASSF8-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.703). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.2, -10.0); signed map (-25.8, -27.7). **Vector** length 68.7, 15.3% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cellular response to chemical stress* (reactome, mean cos +0.50 to 9); *proteasome* (control, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.1 | +10.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +11.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.0 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +8.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +5.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | -17.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -5.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | beta-1,4-N-acetyl-galactosaminyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:57,623,409-57,633,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | beta1-4GalNAc-T; previously GALGT, SPG26 |
| Gene groups (HGNC) | Beta 4-glycosyltransferases |
| Reactome | 4 pathways, smallest: Glycosphingolipid biosynthesis; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00973](https://www.uniprot.org/uniprotkb/Q00973) (Beta-1,4 N-acetylgalactosaminyltransferase 1):

> Involved in the biosynthesis of gangliosides GM2, GD2, GT2 and GA2 from GM3, GD3, GT3 and GA3, respectively.

**Summary**, from NCBI Gene [2583](https://www.ncbi.nlm.nih.gov/gene/2583):

> GM2 and GD2 gangliosides are sialic acid-containing glycosphingolipids. GalNAc-T is the enzyme involved in the biosynthesis of G(M2) and G(D2) glycosphingolipids. GalNAc-T catalyzes the transfer of GalNAc into G(M3) and G(D3) by a beta-1,4 linkage, resulting in the synthesis of G(M2) and G(D2), respectively. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Feb 2013]

**Accessions** — [HGNC:4117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4117) · Entrez [2583](https://www.ncbi.nlm.nih.gov/gene/2583) · UniProt [Q00973](https://www.uniprot.org/uniprotkb/Q00973) · Ensembl [ENSG00000135454](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135454)

## Data

Gene col 5708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5708); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5708]; `tensor/DDL_lfc|DDL_z.npy` [5708]; `embed/gene_vectors.npy` [5708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5708 or target_col == 5708). Every well: [[B4GALNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/B4GALNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
