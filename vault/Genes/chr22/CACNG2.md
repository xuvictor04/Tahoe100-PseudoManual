---
symbol: "CACNG2"
type: "gene"
col: 9375
ensembl_id: "ENSG00000166862"
name: "calcium voltage-gated channel auxiliary subunit gamma 2"
location: "22q12.3"
module: 21
arm: "+"
pooled_cpm: 3.42
n_lines_expressing: 41
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CACNG2

*calcium voltage-gated channel auxiliary subunit gamma 2* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 82.2× (z +24.9, q 0e+00, up in 15 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 9.76× (z +18.2, q 0e+00, up in 24 of 26 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.121×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.159×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLKP1-1]] (+0.74, fdr 7e-06), [[TRD-AS1]] (+0.67, fdr 7e-06), [[ENTHD1]] (+0.65, fdr 1e-05); moves opposite to [[ICE1]] (-0.48, fdr 9e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[KCND2]] → it (grade B ⚠); 7 go from it, the strongest it → [[NEK5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **82.2×** | +24.9 | 0e+00 | 15/15 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **84.0×** | +24.1 | 0e+00 | 7/7 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **50.0×** | +20.5 | 0e+00 | 7/7 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **9.76×** | +18.2 | 0e+00 | 24/26 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **6.31×** | +10.4 | 2e-23 | 19/25 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.51×** | +10.1 | 7e-22 | 17/26 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **5.41×** | +9.2 | 3e-18 | 13/16 (J82, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **20.4×** | +8.9 | 3e-17 | 5/6 (NCI-H2347, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.56×** | +8.6 | 5e-16 | 21/31 (SNU-423, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.57×** | +7.2 | 3e-11 | 18/29 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **3.74×** | +7.2 | 3e-11 | 18/29 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +6.3 | 1e-08 | 12/19 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **3.91×** | +5.5 | 2e-06 | 18/30 (C32, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.56×** | +5.3 | 4e-06 | 18/36 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.65×** | +5.3 | 4e-06 | 7/20 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.47×** | +5.1 | 1e-05 | 11/25 (A-172, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.82×** | +4.8 | 4e-05 | 15/33 (NCI-H2347, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.005 | 12/34 (PANC-1, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.55×** | +3.8 | 0.005 | 8/28 (LoVo, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.82×** | +3.4 | 0.017 | 3/29 (NCI-H460, J82, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.87×** | +3.4 | 0.020 | 10/27 (NCI-H2347, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +3.1 | 0.040 | 6/28 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9375.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (SHP-77 0.121×; ⚠ cell-cycle shift, explains ~25% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SHP-77 0.159×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.547× | -3.3 | 0.43 | 5/33 (RPMI-7951, HOP62, …) | top dose only | plate-row cell shift |
| [[Filgotinib (drug)]] 5 µM |  | 0.569× | -3.2 | 0.43 | 8/37 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 5.05 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 101× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 9.26× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 2.43 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 395× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 28.8× (z +10.1) | — |
| [[J82 (line)]] | alt | 8.04 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.3× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 3.25 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 50.3× (z +12.6) | — |
| [[A-172 (line)]] | wt | 2.51 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 51.7× (z +13.1) | — |
| [[C32 (line)]] | wt | 5.32 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 160× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 3.09 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 83.7× (z +12.2) | — |
| [[NCI-H2347 (line)]] | alt | 6.52 | 2 | 0 | [[Selinexor (drug)]] 5 µM 11.6× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 48.7 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.121× (z -12.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.159× (z -10.6) |
| [[SW 900 (line)]] | alt | 6.09 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 55.4× (z +11.2) | — |
| [[A549 (line)]] | wt | 4.99 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 34.8× (z +9.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 4.82 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 73.5× (z +8.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 2.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 81.9× (z +9.8) | — |
| [[LoVo (line)]] | wt | 1.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 75.1× (z +11.6) | — |
| [[PANC-1 (line)]] | alt | 1.46 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.8× (z +8.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 7.73 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 77.1× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 3.38 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.5× (z +11.8) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 0.630 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.927 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.861 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.698 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.970 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.896 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.728 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.890 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.823 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLKP1-1]] | +0.74 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[TRD-AS1]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[ENTHD1]] | +0.65 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[SNAP25-AS1]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[C12orf50]] | +0.61 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[RBMS3-AS3]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[GRIA4]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 | pathway: Glutamate binding, activation of AMPA receptors and synaptic plasticity; STRING 975 |
| [[MROH8]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[BTG1-DT]] | +0.59 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SFRP4]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[KIAA2012]] | +0.59 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[LINC02603]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICE1]] | -0.48 | -0.37 / -0.52 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCND2]] | B | KCND2 activity raises CACNG2's level | lines that do not express KCND2 (32) vs lines expressing it (18) | 2.05× lower at baseline in the lines without KCND2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, SYT4, DCT; maybe low, not absent |
| [[KLKP1-1]] | B | KLKP1-1 activity raises CACNG2's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without KLKP1-1 | 0.032 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[SSTR2]] | B | SSTR2 activity raises CACNG2's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without SSTR2 | 0.072 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[NOD2]] | B | NOD2 activity raises CACNG2's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 1.69× lower at baseline in the lines without NOD2 | 0.083 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[ANK1]] | B | ANK1 activity raises CACNG2's level | lines that do not express ANK1 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without ANK1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LHX1, GPR173; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEK5]] | B | CACNG2 activity lowers NEK5's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.95× higher at baseline in the lines without CACNG2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[TP53TG5]] | B | CACNG2 activity lowers TP53TG5's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.41× higher at baseline in the lines without CACNG2 | 0.024 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[GATM]] | B | CACNG2 activity lowers GATM's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 2.47× higher at baseline in the lines without CACNG2 | 0.027 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[DLGAP1-AS1]] | B | CACNG2 activity lowers DLGAP1-AS1's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.83× higher at baseline in the lines without CACNG2 | 0.050 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[POU5F2]] | B | CACNG2 activity lowers POU5F2's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.32× higher at baseline in the lines without CACNG2 | 0.079 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[GNAL]] | B | CACNG2 activity lowers GNAL's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 2.50× higher at baseline in the lines without CACNG2 | 0.079 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |
| [[KLKP1-1]] | B | CACNG2 activity raises KLKP1-1's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.99× lower at baseline in the lines without CACNG2 | 0.092 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.457). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.5, 31.3); signed map (37.7, 7.5). **Vector** length 58.8, 12.3% of its response variance represented; |z| ≥ 3 in 669 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.7 | +24.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +24.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +20.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +18.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.1 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +3.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +5.1 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -1.7 | +0.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | +1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.0 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel auxiliary subunit gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:36,560,857-36,703,752 (-) |
| Ensembl biotype | protein_coding |
| Also known as | stargazin, MGC138502, MGC138504 |
| Gene groups (HGNC) | Calcium channel auxiliary gamma subunits |
| Reactome | 7 pathways, smallest: LGI-ADAM interactions; Presynaptic depolarization and calcium channel opening; Glutamate binding, activation of AMPA receptors and synaptic plasticity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y698](https://www.uniprot.org/uniprotkb/Q9Y698) (Voltage-dependent calcium channel gamma-2 subunit):

> Regulates the trafficking and gating properties of AMPA-selective glutamate receptors (AMPARs). Promotes their targeting to the cell membrane and synapses and modulates their gating properties by slowing their rates of activation, deactivation and desensitization. Does not show subunit-specific AMPA receptor regulation and regulates all AMPAR subunits. Thought to stabilize the calcium channel in an inactivated (closed) state.

**Summary**, from NCBI Gene [10369](https://www.ncbi.nlm.nih.gov/gene/10369):

> The protein encoded by this gene is a type I transmembrane AMPA receptor regulatory protein (TARP). TARPs regulate both trafficking and channel gating of the AMPA receptors. The AMPA subtype of ionotropic glutamate receptors are ligand gated ion channels that are typically activated by glutamate released from presynaptic neuron terminals and mediate fast neurotransmission in excitatory synapses. TARPs thus play an important role in synaptic plasticity, learning and memory. Mutations in this …

**Accessions** — [HGNC:1406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1406) · Entrez [10369](https://www.ncbi.nlm.nih.gov/gene/10369) · UniProt [Q9Y698](https://www.uniprot.org/uniprotkb/Q9Y698) · Ensembl [ENSG00000166862](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166862)

## Data

Gene col 9375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9375); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9375]; `tensor/DDL_lfc|DDL_z.npy` [9375]; `embed/gene_vectors.npy` [9375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9375 or target_col == 9375). Every well: [[CACNG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
