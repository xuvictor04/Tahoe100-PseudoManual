---
symbol: "FAP"
type: "gene"
col: 1208
ensembl_id: "ENSG00000078098"
name: "fibroblast activation protein alpha"
location: "2q24.2"
module: 121
arm: "+"
pooled_cpm: 20.81
n_lines_expressing: 25
n_dd_up: 27
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 14
direction_downstream: 11
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# FAP

*fibroblast activation protein alpha* — 2q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.32× (z +26.1, q 0e+00, up in 13 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.406× (z -9.1, q 6e-17, down in 17 of 23 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA2D1]] (+0.69, fdr 1e-05), [[MAGI2-AS3]] (+0.66, fdr 1e-04), [[MIR548XHG]] (+0.65, fdr 1e-05); moves opposite to [[RNF216P1]] (-0.56, fdr 8e-05), [[ATP7B]] (-0.54, fdr 1e-04), [[ANKS6]] (-0.51, fdr 1e-04).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[LINC02492]] → it (grade B ⚠); 11 go from it, the strongest it → [[LINC02268]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.32×** | +26.1 | 0e+00 | 13/21 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.24×** | +16.6 | 0e+00 | 12/21 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.62×** | +15.3 | 0e+00 | 14/22 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.55×** | +11.7 | 1e-29 | 4/14 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +10.9 | 2e-25 | 10/22 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +10.6 | 2e-24 | 6/17 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.63×** | +9.3 | 9e-19 | 10/22 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.86×** | +8.8 | 1e-16 | 11/23 (A-172, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +7.9 | 1e-13 | 1/11 (HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +5.6 | 1e-06 | 9/22 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.76×** | +5.3 | 5e-06 | 2/9 (A-172, NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +5.1 | 2e-05 | 4/19 (NCI-H1573, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +4.5 | 3e-04 | 7/23 (NCI-H460, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.2 | 9e-04 | 5/22 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.50×** | +4.0 | 0.002 | 7/22 (RPMI-7951, hTERT-HPNE, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.91×** | +3.4 | 0.025 | 3/22 (hTERT-HPNE, RPMI-7951, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.026 | 6/22 (C32, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +3.3 | 0.026 | 4/21 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.026 | 4/22 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.037 | 3/21 (BT-474, HS-578T, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.041 | 1/22 (NCI-H460) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.406×** | -9.1 | 6e-17 | 17/23 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.473×** | -7.5 | 1e-11 | 18/23 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.523×** | -6.5 | 1e-08 | 17/23 (A-427, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.583×** | -5.4 | 7e-06 | 13/21 (HEC-1-A, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.594×** | -5.3 | 2e-05 | 13/23 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.415×** | -4.6 | 3e-04 | 13/22 (A-427, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.010 | 6/22 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.776×** | -3.6 | 0.019 | 6/23 (BT-474, SHP-77, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.730×** | -3.2 | 0.091 | 5/23 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -3.1 | 0.094 | 9/22 (LOX-IMVI, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 194 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0645× (z -24.4) |
| [[LOX-IMVI (line)]] | wt | 195 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0507× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 9.11 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 184× (z +22.4) | — |
| [[HEC-1-A (line)]] | alt | 5.83 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 29.0× (z +16.7) | [[Pimozide (drug)]] 0.5 µM 0.0894× (z -8.5) ⚠ transcription drop |
| [[RPMI-7951 (line)]] | alt | 261 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -15.1) |
| [[C32 (line)]] | wt | 95.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -11.4) |
| [[hTERT-HPNE (line)]] | wt | 182 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.260× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 7.98 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.0× (z +17.9) | — |
| [[A-172 (line)]] | wt | 7.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +9.2) | — |
| [[H4 (line)]] | wt | 8.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.8× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 9.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 9.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0871× (z -9.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 8.54 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.05 µM 0.0416× (z -8.5) |
| [[A498 (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.05 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.85 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA2D1]] | +0.69 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[MAGI2-AS3]] | +0.66 | +0.70 / +0.34 | both halves | 1e-04 |  |
| [[MIR548XHG]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP24]] | +0.63 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[MAGI2]] | +0.62 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ARHGAP15]] | +0.61 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[STARD4-AS1]] | +0.61 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[FLRT2]] | +0.60 | +0.66 / +0.36 | both halves | 1e-04 |  |
| [[ZIC1]] | +0.60 | +0.62 / +0.31 | both halves | 2e-04 |  |
| [[SPART-AS1]] | +0.59 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[LINC01687]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[IPO9-AS1]] | +0.59 | +0.55 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF216P1]] | -0.56 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ATP7B]] | -0.54 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[ANKS6]] | -0.51 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[WASF3]] | -0.50 | -0.47 / -0.21 | both halves | 7e-04 |  |
| [[NBPF3]] | -0.50 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[AKTIP]] | -0.50 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[SPTLC2]] | -0.50 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[MFSD9]] | -0.49 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[MKRN2]] | -0.49 | -0.46 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 5, C 9. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02492]] | B | LINC02492 activity raises FAP's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 2.81× lower at baseline in the lines without LINC02492 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers FAP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[VCAN]] | B | VCAN activity raises FAP's level | lines that do not express VCAN (28) vs lines expressing it (22) | 3.06× lower at baseline in the lines without VCAN | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX |
| [[DDX3Y]] | B | DDX3Y activity raises FAP's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 2.08× lower at baseline in the lines without DDX3Y | 0.081 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[HDAC6]] | B | HDAC6 activity raises FAP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NETO1]] | C | NETO1 activity raises FAP's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 7.12× lower at baseline in the lines without NETO1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises FAP's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 4.91× lower at baseline in the lines without LINC01687 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises FAP's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 3.61× lower at baseline in the lines without TRPC4 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[LINC02941]] | C | LINC02941 activity raises FAP's level | lines that do not express LINC02941 (34) vs lines expressing it (16) | 4.05× lower at baseline in the lines without LINC02941 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, CHL1, COL19A1; co-absent with the target |
| [[LINC02240]] | C | LINC02240 activity raises FAP's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 3.14× lower at baseline in the lines without LINC02240 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises FAP's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 4.02× lower at baseline in the lines without PRRX1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[NFATC4]] | C | NFATC4 activity raises FAP's level | lines that do not express NFATC4 (17) vs lines expressing it (33) | 3.14× lower at baseline in the lines without NFATC4 | 0.060 | ⚠ within organs, on part of the lines; also absent: ANK3, ENSG00000227486, PKHD1; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02268]] | B | FAP activity raises LINC02268's level | lines that do not express FAP (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without FAP | 0.014 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5 |
| [[MAD2L1-DT]] | B | FAP activity raises MAD2L1-DT's level | lines that do not express FAP (25) vs lines expressing it (25) | 1.63× lower at baseline in the lines without FAP | 0.029 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5 |
| [[LINC01138]] | B | FAP activity raises LINC01138's level | lines that do not express FAP (25) vs lines expressing it (25) | 1.57× lower at baseline in the lines without FAP | 0.030 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5 |
| [[LAMA2]] | B | FAP activity raises LAMA2's level | lines that do not express FAP (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without FAP | 0.090 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5 |
| [[PCNX4-DT]] | B | FAP activity raises PCNX4-DT's level | lines that do not express FAP (25) vs lines expressing it (25) | 1.29× lower at baseline in the lines without FAP | 0.097 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5 |
| [[TWIST1]] | C | FAP activity raises TWIST1's level | lines that do not express FAP (25) vs lines expressing it (25) | 6.53× lower at baseline in the lines without FAP | 0.011 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5; co-absent with the target |
| [[LINC00882]] | C | FAP activity raises LINC00882's level | lines that do not express FAP (25) vs lines expressing it (25) | 2.89× lower at baseline in the lines without FAP | 0.016 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5; co-absent with the target |
| [[TRPC4]] | C | FAP activity raises TRPC4's level | lines that do not express FAP (25) vs lines expressing it (25) | 3.16× lower at baseline in the lines without FAP | 0.018 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5; co-absent with the target |
| [[JAM2]] | C | FAP activity raises JAM2's level | lines that do not express FAP (25) vs lines expressing it (25) | 2.65× lower at baseline in the lines without FAP | 0.062 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5; co-absent with the target |
| [[LINC01687]] | C | FAP activity raises LINC01687's level | lines that do not express FAP (25) vs lines expressing it (25) | 3.94× lower at baseline in the lines without FAP | 0.081 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5; co-absent with the target |
| [[LINC01060]] | C | FAP activity raises LINC01060's level | lines that do not express FAP (25) vs lines expressing it (25) | 2.95× lower at baseline in the lines without FAP | 0.089 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.711). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.6, 24.7); signed map (43.4, 25.6). **Vector** length 67.6, 16.4% of its response variance represented; |z| ≥ 3 in 669 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +16.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +26.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.0 | +11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +8.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.2 | +0.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.2 | +4.0 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.0 | -9.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | fibroblast activation protein alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.2 — chr2:162,170,684-162,245,151 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DPPIV |
| Gene groups (HGNC) | DASH family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12884](https://www.uniprot.org/uniprotkb/Q12884) (Prolyl endopeptidase FAP):

> Cell surface glycoprotein serine protease that participates in extracellular matrix degradation and involved in many cellular processes including tissue remodeling, fibrosis, wound healing, inflammation and tumor growth. Both plasma membrane and soluble forms exhibit post-proline cleaving endopeptidase activity, with a marked preference for Ala/Ser-Gly-Pro-Ser/Asn/Ala consensus sequences, on substrate such as alpha-2-antiplasmin SERPINF2 and SPRY2. Degrade also gelatin, heat-denatured type I …

**Summary**, from NCBI Gene [2191](https://www.ncbi.nlm.nih.gov/gene/2191):

> The protein encoded by this gene is a homodimeric integral membrane gelatinase belonging to the serine protease family. It is selectively expressed in reactive stromal fibroblasts of epithelial cancers, granulation tissue of healing wounds, and malignant cells of bone and soft tissue sarcomas. This protein is thought to be involved in the control of fibroblast growth or epithelial-mesenchymal interactions during development, tissue repair, and epithelial carcinogenesis. Alternatively spliced …

**Accessions** — [HGNC:3590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3590) · Entrez [2191](https://www.ncbi.nlm.nih.gov/gene/2191) · UniProt [Q12884](https://www.uniprot.org/uniprotkb/Q12884) · Ensembl [ENSG00000078098](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078098)

## Data

Gene col 1208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1208); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1208]; `tensor/DDL_lfc|DDL_z.npy` [1208]; `embed/gene_vectors.npy` [1208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1208 or target_col == 1208). Every well: [[FAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
