---
symbol: "EBF2"
type: "gene"
col: 13305
ensembl_id: "ENSG00000221818"
name: "EBF transcription factor 2"
location: "8p21.2"
module: 19
arm: "+"
pooled_cpm: 2.56
n_lines_expressing: 32
n_dd_up: 30
n_dd_down: 3
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 6
direction_downstream: 16
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# EBF2

*EBF transcription factor 2* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 6.82× (z +23.4, q 0e+00, up in 23 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.623× (z -4.1, q 0.024, down in 10 of 23 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JAKMIP1]] (+0.68, fdr 7e-06), [[CACNG7]] (+0.67, fdr 2e-05), [[CNKSR2]] (+0.66, fdr 7e-06); moves opposite to [[RRAGB]] (-0.54, fdr 7e-05), [[TCTN1]] (-0.54, fdr 4e-04), [[RNF146]] (-0.53, fdr 3e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 16 go from it, the strongest it → [[NRXN3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **6.82×** | +23.4 | 0e+00 | 23/24 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **10.9×** | +20.6 | 0e+00 | 25/27 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.10×** | +19.8 | 0e+00 | 15/19 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.48×** | +18.4 | 0e+00 | 25/26 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.81×** | +17.7 | 0e+00 | 24/26 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **6.52×** | +16.2 | 0e+00 | 26/27 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.83×** | +11.6 | 5e-29 | 19/19 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.42×** | +10.2 | 1e-22 | 0/1 | all doses, flat | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.17×** | +9.9 | 2e-21 | 1/7 (SNU-423) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.66×** | +9.6 | 3e-20 | 2/4 (NCI-H2030, A549) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **5.60×** | +7.8 | 4e-13 | 18/20 (NCI-H460, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.46×** | +7.7 | 5e-13 | 11/13 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.44×** | +7.7 | 8e-13 | 11/21 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +7.5 | 3e-12 | 6/13 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.42×** | +7.3 | 1e-11 | 9/16 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.3 | 6e-04 | 1/24 (NCI-H1573) | top dose only |  |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.59×** | +4.0 | 0.002 | 1/15 (A549) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +3.7 | 0.006 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -4.1 | 0.024 | 10/23 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.630×** | -3.8 | 0.034 | 9/21 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.655×** | -3.7 | 0.046 | 8/25 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.657× | -3.1 | 0.20 | 2/25 (KATO III, SNU-1) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -3.1 | 0.20 | 6/27 (NCI-H2030, NCI-H23, …) | inconsistent across doses |  |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.707× | -3.0 | 0.25 | 2/20 (hTERT-HPNE, NCI-H460) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.09 | 5 | 8 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.15× (z +11.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0419× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 32.3 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0299× (z -23.2) |
| [[A-427 (line)]] | wt | 6.06 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 15.5× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0644× (z -9.8) |
| [[A549 (line)]] | wt | 7.98 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0357× (z -16.6) |
| [[NCI-H2030 (line)]] | alt | 8.53 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.84× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.0660× (z -16.0) |
| [[PANC-1 (line)]] | alt | 1.16 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 26.3× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 6.52 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0712× (z -9.7) |
| [[A-172 (line)]] | wt | 1.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.9× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 3.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.0× (z +9.8) | — |
| [[LoVo (line)]] | wt | 0.945 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.0× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 1.26 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 37.4× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 5.27 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.65× (z +9.0) | — |
| [[SW480 (line)]] | alt | 0.914 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 32.8× (z +12.1) | — |
| [[A498 (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.713 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.680 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.537 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.578 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.696 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.655 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.729 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.749 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.606 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.652 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.682 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.916 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.586 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.484 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JAKMIP1]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[CACNG7]] | +0.67 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[CNKSR2]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[SFMBT2]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[COL4A4]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[TMEM170B]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[UNC5D]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TRIM9]] | +0.58 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[GDPGP1]] | +0.57 | +0.36 / +0.52 | both halves | 9e-05 |  |
| [[IL1RAP]] | +0.56 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[LINC00540]] | +0.56 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[EXTL3]] | +0.56 | +0.38 / +0.63 | both halves | 7e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAGB]] | -0.54 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[TCTN1]] | -0.54 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[RNF146]] | -0.53 | -0.29 / -0.50 | both halves | 3e-04 |  |
| [[ARMCX5-GPRASP2]] | -0.51 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[TRMT13]] | -0.50 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[ARFGAP2]] | -0.50 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[ARMCX4]] | -0.49 | -0.14 / -0.57 | ⚠ one half (not replicated) | 0.002 |  |
| [[N4BP2L2]] | -0.48 | -0.28 / -0.45 | both halves | 3e-04 |  |
| [[ZNF91]] | -0.48 | -0.26 / -0.34 | both halves | 3e-04 |  |
| [[PHC3]] | -0.48 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[GABPB2]] | -0.48 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[QTRT1]] | -0.48 | -0.38 / -0.33 | both halves | 1e-04 |  |
| [[C15orf40]] | -0.48 | -0.31 / -0.33 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers EBF2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.4% of all compounds | 0.008 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NRXN3]] | B | NRXN3 activity raises EBF2's level | lines that do not express NRXN3 (23) vs lines expressing it (27) | 1.88× lower at baseline in the lines without NRXN3 | 0.010 | ⚠ within organs, on part of the lines; also absent: RGS7, FGF13, ENSG00000255983 |
| [[COL4A4]] | B | COL4A4 activity raises EBF2's level | lines that do not express COL4A4 (28) vs lines expressing it (22) | 1.79× lower at baseline in the lines without COL4A4 | 0.041 | ⚠ within organs, on part of the lines; also absent: COL4A3, LHX2, EPB41L4A |
| [[COL4A3]] | B | COL4A3 activity raises EBF2's level | lines that do not express COL4A3 (29) vs lines expressing it (21) | 1.78× lower at baseline in the lines without COL4A3 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL4A4, LHX2, MAPK4 |
| [[SLC6A17]] | B | SLC6A17 activity raises EBF2's level | lines that do not express SLC6A17 (28) vs lines expressing it (22) | 1.97× lower at baseline in the lines without SLC6A17 | 0.058 | ⚠ within organs, on part of the lines; also absent: TWIST1, LINC00470, MAGEA3-DT |
| [[GNAO1]] | B | GNAO1 activity raises EBF2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 1.74× lower at baseline in the lines without GNAO1 | 0.087 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17 |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRXN3]] | B | EBF2 activity raises NRXN3's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without EBF2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[SUSD4]] | B | EBF2 activity raises SUSD4's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.79× lower at baseline in the lines without EBF2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[MTUS2]] | B | EBF2 activity raises MTUS2's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.63× lower at baseline in the lines without EBF2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[MMP17]] | B | EBF2 activity raises MMP17's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without EBF2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[SFMBT2]] | B | EBF2 activity raises SFMBT2's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.73× lower at baseline in the lines without EBF2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[EYA2]] | B | EBF2 activity raises EYA2's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without EBF2 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[SYN1]] | B | EBF2 activity strengthens SYN1's drug response | lines that do not express EBF2 (17) vs lines expressing it (28) | the lines without EBF2 respond 0.50× as strongly (z diff +1.93); strongest at Belinostat 5 µM: 1.60x vs 4.63x (z diff +3.3) | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[B3GALT1]] | B | EBF2 activity raises B3GALT1's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.97× lower at baseline in the lines without EBF2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[KCNK13]] | B | EBF2 activity raises KCNK13's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 1.51× lower at baseline in the lines without EBF2 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[COL4A3]] | B | EBF2 activity raises COL4A3's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without EBF2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[NRG2]] | B | EBF2 activity raises NRG2's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.37× lower at baseline in the lines without EBF2 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |
| [[GNAO1]] | B | EBF2 activity raises GNAO1's level | lines that do not express EBF2 (18) vs lines expressing it (32) | 2.06× lower at baseline in the lines without EBF2 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000249738, LMX1B, CAPN14; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.403). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.4, 39.5); signed map (40.3, 47.6). **Vector** length 58.2, 12.9% of its response variance represented; |z| ≥ 3 in 787 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +23.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +5.3 | +9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +19.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +4.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | -1.5 | +3.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | EBF transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:25,841,725-26,045,413 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11500, COE2 |
| Gene groups (HGNC) | EBF transcription factors; IPT domain containing |
| Reactome | 3 pathways, smallest: Transcriptional regulation of brown and beige adipocyte differentiation; Transcriptional regulation of brown and beige adipocyte differentiation by EBF2; Adipogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HAK2](https://www.uniprot.org/uniprotkb/Q9HAK2) (Transcription factor COE2):

> Transcription factor that, in osteoblasts, activates the decoy receptor for RANKL, TNFRSF11B, which in turn regulates osteoclast differentiation. Acts in synergy with the Wnt-responsive LEF1/CTNNB1 pathway. Recognizes variations of the palindromic sequence 5'-ATTCCCNNGGGAATT-3' (By similarity).

**Summary**, from NCBI Gene [64641](https://www.ncbi.nlm.nih.gov/gene/64641):

> The protein encoded by this gene belongs to the COE (Collier/Olf/EBF) family of non-basic, helix-loop-helix transcription factors that have a well conserved DNA binding domain. The COE family proteins play an important role in variety of developmental processes. Studies in mouse suggest that this gene may be involved in the differentiation of osteoblasts. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:19090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19090) · Entrez [64641](https://www.ncbi.nlm.nih.gov/gene/64641) · UniProt [Q9HAK2](https://www.uniprot.org/uniprotkb/Q9HAK2) · Ensembl [ENSG00000221818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221818)

## Data

Gene col 13305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13305); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13305]; `tensor/DDL_lfc|DDL_z.npy` [13305]; `embed/gene_vectors.npy` [13305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13305 or target_col == 13305). Every well: [[EBF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EBF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
