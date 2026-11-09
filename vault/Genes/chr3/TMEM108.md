---
symbol: "TMEM108"
type: "gene"
col: 6941
ensembl_id: "ENSG00000144868"
name: "transmembrane protein 108"
location: "3q22.1"
module: 82
arm: "+"
pooled_cpm: 7.84
n_lines_expressing: 27
n_dd_up: 34
n_dd_down: 3
n_dd_up_clean: 23
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 12
direction_downstream: 3
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# TMEM108

*transmembrane protein 108* — 3q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.76× (z +30.7, q 0e+00, up in 12 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Larotrectinib (drug)]] 5 µM: 0.764× (z -4.8, q 0.001, down in 7 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEX15]] (+0.73, fdr 7e-06), [[ST6GALNAC3]] (+0.69, fdr 1e-05), [[NCAM2]] (+0.68, fdr 7e-06).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 3 go from it, the strongest it → [[ENPP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6941.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.76×** | +30.7 | 0e+00 | 12/21 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.29×** | +21.0 | 0e+00 | 23/23 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **4.25×** | +18.2 | 0e+00 | 23/24 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.64×** | +16.2 | 0e+00 | 22/23 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.60×** | +16.1 | 0e+00 | 22/23 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.29×** | +15.0 | 0e+00 | 6/15 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.34×** | +13.4 | 7e-39 | 3/10 (HOP62, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.85×** | +13.0 | 8e-37 | 23/24 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.12×** | +12.1 | 5e-32 | 23/23 (NCI-H2030, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +11.8 | 2e-30 | 7/20 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.46×** | +11.3 | 5e-28 | 17/21 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.41×** | +10.6 | 9e-25 | 8/20 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.15×** | +9.2 | 1e-18 | 4/11 (HOP62, SNU-423, …) | all doses, flat | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **4.02×** | +9.1 | 3e-18 | 20/23 (NCI-H2030, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.2 | 2e-11 | 2/23 (HOP62, BT-474) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.91×** | +6.9 | 2e-10 | 3/23 (BT-474, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +6.2 | 2e-08 | 5/23 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.38×** | +5.6 | 6e-07 | 3/21 (SNU-423, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6941.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Larotrectinib (drug)]] 5 µM |  | **0.764×** | -4.8 | 0.001 | 7/23 (A-427, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.733×** | -3.9 | 0.023 | 8/23 (NCI-H23, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.755×** | -3.5 | 0.075 | 7/22 (NCI-H23, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | 0.769× | -3.2 | 0.19 | 1/23 (NCI-H2030) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6941. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 24.3 | 5 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 9.93× (z +12.3) | [[Digitoxin (drug)]] 0.5 µM 0.0285× (z -19.0) |
| [[C32 (line)]] | wt | 43.3 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 7.16× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0759× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 9.51 | 5 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 16.4× (z +13.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0657× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~56% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0856× (z -11.9) |
| [[HOP62 (line)]] | alt | 2.87 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 44.6× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 5.48 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 41.8× (z +12.6) | — |
| [[A-427 (line)]] | wt | 137 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.426× (z -10.4) |
| [[H4 (line)]] | wt | 15.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 19.8× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 20.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 10.2× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 1.98 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 22.6× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 3.60 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 26.5× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.49 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 17.9× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 4.56 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.50× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 45.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0618× (z -17.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 81.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -11.5) |
| [[J82 (line)]] | alt | 2.03 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 25.9× (z +8.6) | — |
| [[NCI-H1792 (line)]] | alt | 2.41 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 22.5× (z +8.5) | — |
| [[A-172 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.974 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6941), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEX15]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[ST6GALNAC3]] | +0.69 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CTNNA2]] | +0.67 | +0.61 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ASXL3]] | +0.65 | +0.39 / +0.75 | both halves | 6e-05 |  |
| [[SNTG2]] | +0.65 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[PDGFD]] | +0.65 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[GUCY1B1]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[GRIA2]] | +0.64 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[KCNH7]] | +0.63 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[ERBB4]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[GNAO1]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 3, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMEM108's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[B3GALT1]] | B | B3GALT1 activity raises TMEM108's level | lines that do not express B3GALT1 (20) vs lines expressing it (30) | 2.77× lower at baseline in the lines without B3GALT1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ANTXR1, LINC00882, LINC01695; maybe low, not absent |
| [[MAN1C1]] | B | MAN1C1 activity raises TMEM108's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without MAN1C1 | 0.087 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[FREM2]] | C | FREM2 activity raises TMEM108's level | lines that do not express FREM2 (26) vs lines expressing it (24) | 3.31× lower at baseline in the lines without FREM2 | 0.011 | ⚠ within organs, on part of the lines; also absent: NELL2, ANKRD20A11P, KCNH7; maybe low, not absent; co-absent with the target |
| [[NEGR1]] | C | NEGR1 activity raises TMEM108's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 3.16× lower at baseline in the lines without NEGR1 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises TMEM108's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.46× lower at baseline in the lines without CTNNA2 | 0.058 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[SLITRK6]] | C | SLITRK6 activity raises TMEM108's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.82× lower at baseline in the lines without SLITRK6 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; co-absent with the target |
| [[SLC6A17]] | C | SLC6A17 activity raises TMEM108's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 3.01× lower at baseline in the lines without SLC6A17 | 0.062 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT; co-absent with the target |
| [[GNAO1]] | C | GNAO1 activity raises TMEM108's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.24× lower at baseline in the lines without GNAO1 | 0.080 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17; co-absent with the target |
| [[SYT11]] | C | SYT11 activity raises TMEM108's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 2.76× lower at baseline in the lines without SYT11 | 0.089 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1; co-absent with the target |
| [[TRIM9]] | C | TRIM9 activity raises TMEM108's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 2.71× lower at baseline in the lines without TRIM9 | 0.099 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1; co-absent with the target |
| [[DPYSL5]] | C | DPYSL5 activity raises TMEM108's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without DPYSL5 | 0.099 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP2]] | B | TMEM108 activity raises ENPP2's level | lines that do not express TMEM108 (23) vs lines expressing it (27) | 2.51× lower at baseline in the lines without TMEM108 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: TWIST1, FYB1, GATA3; maybe low, not absent |
| [[HMCN1]] | C | TMEM108 activity raises HMCN1's level | lines that do not express TMEM108 (23) vs lines expressing it (27) | 3.66× lower at baseline in the lines without TMEM108 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: TWIST1, FYB1, GATA3; maybe low, not absent; co-absent with the target |
| [[CHMP1B2P]] | C | TMEM108 activity raises CHMP1B2P's level | lines that do not express TMEM108 (23) vs lines expressing it (27) | 3.11× lower at baseline in the lines without TMEM108 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: TWIST1, FYB1, GATA3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.4, 34.4); signed map (34.9, 33.5). **Vector** length 62.0, 15.1% of its response variance represented; |z| ≥ 3 in 637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.0 | +21.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.2 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +6.6 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +13.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +9.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +3.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 108 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q22.1 — chr3:133,038,391-133,397,775 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RTLN, MGC3040, CT124 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXF1](https://www.uniprot.org/uniprotkb/Q6UXF1) (Transmembrane protein 108):

> Transmembrane protein required for proper cognitive functions. Involved in the development of dentate gyrus (DG) neuron circuitry, is necessary for AMPA receptors surface expression and proper excitatory postsynaptic currents of DG granule neurons. Regulates the organization and stability of the microtubule network of sensory neurons to allow axonal transport. Through the interaction with DST, mediates the docking of the dynein/dynactin motor complex to vesicle cargos for retrograde axonal …

**Summary**, from NCBI Gene [66000](https://www.ncbi.nlm.nih.gov/gene/66000):

> Predicted to be involved in several processes, including cellular response to brain-derived neurotrophic factor stimulus; nervous system development; and regulation of signal transduction. Predicted to be located in somatodendritic compartment. Predicted to be active in axon; endosome; and postsynaptic density. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28451) · Entrez [66000](https://www.ncbi.nlm.nih.gov/gene/66000) · UniProt [Q6UXF1](https://www.uniprot.org/uniprotkb/Q6UXF1) · Ensembl [ENSG00000144868](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144868)

## Data

Gene col 6941: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6941); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6941, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6941]; `tensor/DDL_lfc|DDL_z.npy` [6941]; `embed/gene_vectors.npy` [6941]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6941 or target_col == 6941). Every well: [[TMEM108 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM108.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
