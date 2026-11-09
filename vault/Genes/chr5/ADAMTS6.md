---
symbol: "ADAMTS6"
type: "gene"
col: 545
ensembl_id: "ENSG00000049192"
name: "ADAM metallopeptidase with thrombospondin type 1 motif 6"
location: "5q12.3"
module: 13
arm: "+"
pooled_cpm: 161.59
n_lines_expressing: 25
n_dd_up: 10
n_dd_down: 32
n_dd_up_clean: 8
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 40
direction_downstream: 51
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# ADAMTS6

*ADAM metallopeptidase with thrombospondin type 1 motif 6* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.27× (z +10.5, q 5e-23, up in 8 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.509× (z -8.6, q 4e-15, down in 18 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD3]] (+0.74, fdr 7e-06), [[SPOCK1]] (+0.73, fdr 7e-06), [[BMPER]] (+0.72, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[BMPER]] → it (grade B ⚠); 51 go from it, the strongest it → [[IQCJ-SCHIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 545.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +10.5 | 5e-23 | 8/23 (SK-MEL-2, HT-29, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.16×** | +9.9 | 2e-20 | 10/23 (HT-29, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +9.5 | 3e-19 | 8/23 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.04×** | +9.2 | 7e-18 | 4/24 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.97×** | +8.7 | 5e-16 | 7/23 (HT-29, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +7.3 | 3e-11 | 5/23 (SK-MEL-2, HT-29, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +5.7 | 7e-07 | 8/23 (Panc 03.27, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.28×** | +5.5 | 3e-06 | 6/24 (SK-MEL-2, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.7 | 1e-04 | 5/24 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.3 | 9e-04 | 2/19 (Panc 03.27, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.14 | 10/24 (Panc 03.27, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 545.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.509×** | -8.6 | 4e-15 | 18/23 (NCI-H460, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -7.2 | 1e-10 | 20/23 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.604×** | -6.4 | 3e-08 | 15/23 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.630×** | -5.9 | 5e-07 | 12/23 (HOP62, H4, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.640×** | -5.7 | 2e-06 | 14/23 (H4, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.646×** | -5.6 | 2e-06 | 13/23 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.649×** | -5.5 | 3e-06 | 15/23 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.668×** | -5.1 | 2e-05 | 19/23 (NCI-H460, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.668×** | -5.1 | 2e-05 | 21/23 (hTERT-HPNE, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.680×** | -4.9 | 5e-05 | 7/22 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.682×** | -4.9 | 6e-05 | 14/23 (H4, HOP62, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.770×** | -4.7 | 1e-04 | 14/23 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.694×** | -4.7 | 1e-04 | 11/23 (hTERT-HPNE, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.680×** | -4.5 | 2e-04 | 12/22 (hTERT-HPNE, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.781×** | -4.5 | 3e-04 | 14/23 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.712×** | -4.3 | 6e-04 | 17/23 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.721×** | -4.2 | 0.001 | 14/23 (HOP62, A-172, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 545. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1,187 | 0 | 26 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0918× (z -30.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.119× (z -27.0) |
| [[hTERT-HPNE (line)]] | wt | 1,316 | 0 | 25 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0469× (z -29.1) |
| [[LOX-IMVI (line)]] | wt | 964 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0909× (z -27.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.198× (z -12.9) |
| [[A-172 (line)]] | wt | 770 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0765× (z -21.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.151× (z -11.1) |
| [[HOP62 (line)]] | alt | 81.5 | 0 | 7 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 5 µM 0.156× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 50.1 | 7 (2 ⚠) | 0 | [[Daptomycin (drug)]] 5 µM 7.42× (z +13.2) ⚠ unreliable plate only · without an alert: [[Peretinoin (drug)]] 5 µM 7.31× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 64.9 | 6 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.89× (z +11.2) | — |
| [[H4 (line)]] | wt | 130 | 0 | 4 | — | [[Clobetasol propionate (drug)]] 5 µM 0.119× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 141 | 3 (1 ⚠) | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 3.34× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 333 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 79.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -9.5) |
| [[J82 (line)]] | alt | 130 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 150 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.4) |
| [[Hs 766T (line)]] | wt | 201 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 99.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -11.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.2 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 16.1 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 151 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 67.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 39.2 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 23.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.0 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.5 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 19.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 28.0 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.0 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 24.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 19.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 545), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD3]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SPOCK1]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[BMPER]] | +0.72 | +0.75 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[TMEM200A]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.71 | +0.65 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[FGF5]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[VEGFC]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[NMNAT2]] | +0.68 | +0.72 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LINC01411]] | +0.67 | +0.70 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[CDH13]] | +0.66 | +0.56 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[NALF1]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[PDCD1LG2]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 6, C 34. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPER]] | B | BMPER activity raises ADAMTS6's level | lines that do not express BMPER (21) vs lines expressing it (29) | 3.26× lower at baseline in the lines without BMPER | 0.034 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[SERPIND1]] | B | SERPIND1 activity raises ADAMTS6's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 3.07× lower at baseline in the lines without SERPIND1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers ADAMTS6's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ADAMTS6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ADAMTS6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EVC]] | B | EVC activity raises ADAMTS6's level | lines that do not express EVC (13) vs lines expressing it (37) | 3.79× lower at baseline in the lines without EVC | 0.083 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |
| [[ESM1]] | C | ESM1 activity raises ADAMTS6's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 7.16× lower at baseline in the lines without ESM1 | 5e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises ADAMTS6's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 5.93× lower at baseline in the lines without CDH13 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises ADAMTS6's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 5.00× lower at baseline in the lines without PDCD1LG2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[ABI3BP]] | C | ABI3BP activity raises ADAMTS6's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 4.49× lower at baseline in the lines without ABI3BP | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises ADAMTS6's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 4.16× lower at baseline in the lines without C5orf46 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[HHIP]] | C | HHIP activity raises ADAMTS6's level | lines that do not express HHIP (33) vs lines expressing it (17) | 4.17× lower at baseline in the lines without HHIP | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 14, C 37. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IQCJ-SCHIP1]] | B | ADAMTS6 activity strengthens IQCJ-SCHIP1's drug response | lines that do not express ADAMTS6 (20) vs lines expressing it (22) | the lines without ADAMTS6 respond 0.70× as strongly (z diff +1.77); strongest at Dinaciclib 5 µM: 0.71x vs 0.30x (z diff +4.9) | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; target measured in part of the lines; artifact flags |
| [[RGMB]] | B | ADAMTS6 activity raises RGMB's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without ADAMTS6 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[EVC]] | B | ADAMTS6 activity raises EVC's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 3.50× lower at baseline in the lines without ADAMTS6 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[FRMD6]] | B | ADAMTS6 activity raises FRMD6's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 3.49× lower at baseline in the lines without ADAMTS6 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[SCHIP1]] | B | ADAMTS6 activity raises SCHIP1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.63× lower at baseline in the lines without ADAMTS6 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[SCHIP1]] | B | ADAMTS6 activity strengthens SCHIP1's drug response | lines that do not express ADAMTS6 (19) vs lines expressing it (22) | the lines without ADAMTS6 respond 0.62× as strongly (z diff +1.96); strongest at Dinaciclib 0.5 µM: 0.70x vs 0.44x (z diff +3.4) | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; target measured in part of the lines; artifact flags |
| [[VEPH1]] | B | ADAMTS6 activity raises VEPH1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.59× lower at baseline in the lines without ADAMTS6 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[PRSS23]] | B | ADAMTS6 activity raises PRSS23's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.16× lower at baseline in the lines without ADAMTS6 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[CD44]] | B | ADAMTS6 activity raises CD44's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.80× lower at baseline in the lines without ADAMTS6 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[ADAMTS16]] | B | ADAMTS6 activity raises ADAMTS16's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.80× lower at baseline in the lines without ADAMTS6 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[FHAD1]] | B | ADAMTS6 activity raises FHAD1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 1.42× lower at baseline in the lines without ADAMTS6 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[PDE4DIPP2]] | B | ADAMTS6 activity raises PDE4DIPP2's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.21× lower at baseline in the lines without ADAMTS6 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.4, 14.8); signed map (20.3, 48.0). **Vector** length 113, 36.2% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +6.7 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +9.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.5 | -4.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.4 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | -0.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.7 | -5.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.5 | -6.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.9 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.8 | -5.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -3.7 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | ADAM metallopeptidase with thrombospondin type 1 motif 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:65,148,738-65,481,920 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ADAM-TS6 |
| Gene groups (HGNC) | ADAM metallopeptidases with thrombospondin type 1 motif |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

UniProt [Q9UKP5](https://www.uniprot.org/uniprotkb/Q9UKP5) carries no function annotation.

**Summary**, from NCBI Gene [11174](https://www.ncbi.nlm.nih.gov/gene/11174):

> This gene encodes a member of the ADAMTS (a disintegrin and metalloproteinase with thrombospondin motifs) protein family. Members of the family share several distinct protein modules, including a propeptide region, a metalloproteinase domain, a disintegrin-like domain, and a thrombospondin type 1 (TS) motif. Individual members of this family differ in the number of C-terminal TS motifs, and some have unique C-terminal domains. The encoded preproprotein is proteolytically processed to generate …

**Accessions** — [HGNC:222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:222) · Entrez [11174](https://www.ncbi.nlm.nih.gov/gene/11174) · UniProt [Q9UKP5](https://www.uniprot.org/uniprotkb/Q9UKP5) · Ensembl [ENSG00000049192](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049192)

## Data

Gene col 545: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 545); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 545, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 545]; `tensor/DDL_lfc|DDL_z.npy` [545]; `embed/gene_vectors.npy` [545]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 545 or target_col == 545). Every well: [[ADAMTS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
