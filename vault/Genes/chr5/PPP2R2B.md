---
symbol: "PPP2R2B"
type: "gene"
col: 7985
ensembl_id: "ENSG00000156475"
name: "protein phosphatase 2 regulatory subunit Bbeta"
location: "5q32"
module: 9
arm: "+"
pooled_cpm: 9.73
n_lines_expressing: 27
n_dd_up: 38
n_dd_down: 1
n_dd_up_clean: 30
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PPP2R2B

*protein phosphatase 2 regulatory subunit Bbeta* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 4.02× (z +20.2, q 0e+00, up in 20 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.624× (z -4.9, q 6e-04, down in 11 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (C32 0.0607×, SHP-77 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (C32 0.142×, SHP-77 0.304×; ⚠ cell-cycle shift, explains ~0% of this change); [[Daptomycin (drug)]] 5 µM in 1 line (C32 0.0923×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (C32 0.189×); [[Peretinoin (drug)]] 0.5 µM in 1 line (C32 0.101×); [[Peretinoin (drug)]] 5 µM in 1 line (C32 0.100×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAM2]] (+0.64, fdr 7e-06), [[DMD]] (+0.64, fdr 1e-05), [[MOXD1]] (+0.64, fdr 7e-06); moves opposite to [[RPSAP52]] (-0.47, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[PRUNE2]] → it (grade B ⚠); 10 go from it, the strongest it → [[SESN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7985.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **4.02×** | +20.2 | 0e+00 | 20/23 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.49×** | +18.1 | 0e+00 | 15/21 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.21×** | +14.7 | 0e+00 | 6/13 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.76×** | +13.0 | 9e-37 | 5/10 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +12.4 | 4e-33 | 13/20 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.23×** | +12.0 | 3e-31 | 19/22 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.99×** | +11.2 | 3e-27 | 19/23 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.97×** | +11.2 | 4e-27 | 20/23 (J82, SW 900, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.74×** | +10.3 | 4e-23 | 17/22 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.52×** | +9.5 | 2e-19 | 19/21 (CFPAC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.61×** | +9.1 | 5e-18 | 3/10 (J82, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.23×** | +8.2 | 1e-14 | 11/22 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.03×** | +7.5 | 4e-12 | 12/22 (J82, SW 900, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +6.8 | 4e-10 | 8/20 (HOP62, SW1417, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +6.2 | 2e-08 | 8/18 (A-172, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.81×** | +5.8 | 2e-07 | 7/21 (J82, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.80×** | +5.8 | 2e-07 | 11/20 (C32, J82, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 3e-06 | 6/22 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7985.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (C32 0.0607×, SHP-77 0.228×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (C32 0.142×, SHP-77 0.304×; ⚠ cell-cycle shift, explains ~0% of this change); [[Daptomycin (drug)]] 5 µM in 1 line (C32 0.0923×; ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (C32 0.189×); [[Peretinoin (drug)]] 0.5 µM in 1 line (C32 0.101×); [[Peretinoin (drug)]] 5 µM in 1 line (C32 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.624×** | -4.9 | 6e-04 | 11/22 (C32, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7985. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 104 | 9 | 9 (5 ⚠) | [[Binimetinib (drug)]] 0.5 µM 6.80× (z +11.1) | [[Digitoxin (drug)]] 5 µM 0.0607× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.189× (z -11.2) |
| [[J82 (line)]] | alt | 29.7 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 10.4× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.75 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 15.0× (z +12.6) | — |
| [[HOP62 (line)]] | alt | 3.95 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.9× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 10.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.78× (z +10.2) | — |
| [[A-172 (line)]] | wt | 69.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.250× (z -8.5) |
| [[SHP-77 (line)]] | alt | 111 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 8.15 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.80× (z +11.4) | — |
| [[SW 900 (line)]] | alt | 23.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.84× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 5.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.8× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 3.37 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 15.3× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 2.44 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.19× (z +8.6) | — |
| [[A-427 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7985), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAM2]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[DMD]] | +0.64 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[MOXD1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[GRIA2]] | +0.63 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[UNC5C]] | +0.63 | +0.52 / +0.71 | both halves | 1e-05 |  |
| [[ARHGAP28]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[HMCN1]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[GUCY1B1]] | +0.62 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[TMEM108]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[LDB2]] | +0.61 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[LHFPL3-AS1]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[EGFEM1P]] | +0.59 | +0.58 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSAP52]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRUNE2]] | B | PRUNE2 activity raises PPP2R2B's level | lines that do not express PRUNE2 (30) vs lines expressing it (20) | 2.36× lower at baseline in the lines without PRUNE2 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGF13, SSX1, UTY |
| [[TOP2A]] | B | TOP2A activity lowers PPP2R2B's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SULF1]] | C | SULF1 activity raises PPP2R2B's level | lines that do not express SULF1 (35) vs lines expressing it (15) | 3.05× lower at baseline in the lines without SULF1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00958, LINC01592, TBXT; co-absent with the target |
| [[APOD]] | C | APOD activity raises PPP2R2B's level | lines that do not express APOD (43) vs lines expressing it (7) | 5.27× lower at baseline in the lines without APOD | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LHFPL3-AS1, SOX10, CALCA; co-absent with the target |
| [[TRPM8]] | C | TRPM8 activity raises PPP2R2B's level | lines that do not express TRPM8 (28) vs lines expressing it (22) | 1.88× lower at baseline in the lines without TRPM8 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC01320, LINC02335; maybe low, not absent; co-absent with the target |
| [[GPNMB]] | C | GPNMB activity raises PPP2R2B's level | lines that do not express GPNMB (30) vs lines expressing it (20) | 2.66× lower at baseline in the lines without GPNMB | 0.086 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: IGFBP5, RUNX1T1, CNTN6; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SESN3]] | B | PPP2R2B activity raises SESN3's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without PPP2R2B | 0.025 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent |
| [[GPNMB]] | C | PPP2R2B activity raises GPNMB's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 4.00× lower at baseline in the lines without PPP2R2B | 0.016 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[P2RX7]] | C | PPP2R2B activity raises P2RX7's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 2.51× lower at baseline in the lines without PPP2R2B | 0.024 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[RBP1]] | C | PPP2R2B activity raises RBP1's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without PPP2R2B | 0.025 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[ENPP2]] | C | PPP2R2B activity raises ENPP2's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 2.75× lower at baseline in the lines without PPP2R2B | 0.028 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[GRIK2]] | C | PPP2R2B activity raises GRIK2's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without PPP2R2B | 0.036 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[CFI]] | C | PPP2R2B activity raises CFI's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 2.89× lower at baseline in the lines without PPP2R2B | 0.040 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[PDZRN3]] | C | PPP2R2B activity raises PDZRN3's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 3.12× lower at baseline in the lines without PPP2R2B | 0.055 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[SOX5]] | C | PPP2R2B activity raises SOX5's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 3.68× lower at baseline in the lines without PPP2R2B | 0.060 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |
| [[MOXD1]] | C | PPP2R2B activity raises MOXD1's level | lines that do not express PPP2R2B (23) vs lines expressing it (27) | 2.47× lower at baseline in the lines without PPP2R2B | 0.076 | ⚠ within organs, on part of the lines; also absent: SSTR2, COL5A1, MCAM; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.578). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.3, 30.5); signed map (35.9, 33.8). **Vector** length 64.9, 16.4% of its response variance represented; |z| ≥ 3 in 699 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +20.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +14.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +9.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +5.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +4.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.1 | +4.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 regulatory subunit Bbeta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:146,580,742-147,084,784 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PR55-BETA, PR52B, B55beta; previously SCA12 |
| Gene groups (HGNC) | WD repeat domain containing; Protein phosphatase 2 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00005](https://www.uniprot.org/uniprotkb/Q00005) (Serine/threonine-protein phosphatase 2A 55 kDa regulatory subunit B beta isoform):

> The B regulatory subunit might modulate substrate selectivity and catalytic activity, and might also direct the localization of the catalytic enzyme to a particular subcellular compartment. Within the PP2A holoenzyme complex, isoform 2 is required to promote pro-apoptotic activity (By similarity). Isoform 2 regulates neuronal survival through the mitochondrial fission and fusion balance (By similarity).

**Summary**, from NCBI Gene [5521](https://www.ncbi.nlm.nih.gov/gene/5521):

> The product of this gene belongs to the phosphatase 2 regulatory subunit B family. Protein phosphatase 2 is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The B regulatory subunit might modulate substrate selectivity and catalytic activity. This …

**Accessions** — [HGNC:9305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9305) · Entrez [5521](https://www.ncbi.nlm.nih.gov/gene/5521) · UniProt [Q00005](https://www.uniprot.org/uniprotkb/Q00005) · Ensembl [ENSG00000156475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156475)

## Data

Gene col 7985: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7985); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7985, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7985]; `tensor/DDL_lfc|DDL_z.npy` [7985]; `embed/gene_vectors.npy` [7985]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7985 or target_col == 7985). Every well: [[PPP2R2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
