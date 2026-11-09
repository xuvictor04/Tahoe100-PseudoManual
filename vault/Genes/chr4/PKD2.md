---
symbol: "PKD2"
type: "gene"
col: 4016
ensembl_id: "ENSG00000118762"
name: "polycystin 2, transient receptor potential cation channel"
location: "4q22.1"
module: 18
arm: "+"
pooled_cpm: 60.82
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 21
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PKD2

*polycystin 2, transient receptor potential cation channel* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 1.25× (z +4.1, q 0.009, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -14.0, q 1e-41, down in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.564× (z -10.5, q 4e-23, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF11]] (+0.64, fdr 7e-06), [[ZNRF2P2]] (+0.61, fdr 1e-05), [[LSM6]] (+0.61, fdr 1e-05); moves opposite to [[ATOSB]] (-0.51, fdr 1e-04), [[MKNK1]] (-0.50, fdr 9e-05), [[MYO7A]] (-0.49, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDGFL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.009 | 20/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.0 | 0.009 | 26/48 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.0 | 0.009 | 18/48 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.009 | 20/48 (hTERT-HPNE, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.009 | 21/47 (SW480, H4, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.15× | +3.8 | 0.015 | 21/48 (LoVo, LS 180, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.015 | 23/49 (SW480, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.22×** | +3.6 | 0.019 | 18/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.13 | 14/48 (hTERT-HPNE, LS 180, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.13 | 14/48 (LS 180, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.582×** | -14.0 | 1e-41 | 41/48 (NCI-H460, J82, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.564×** | -10.5 | 4e-23 | 37/48 (SW480, A-427, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.371×** | -9.5 | 6e-19 | 40/49 (HOP62, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.593×** | -9.2 | 8e-18 | 35/48 (AN3 CA, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.619×** | -8.7 | 3e-16 | 35/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.624×** | -8.6 | 8e-16 | 31/48 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -7.6 | 3e-12 | 29/48 (A-427, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.660×** | -7.5 | 5e-12 | 33/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.684×** | -6.6 | 2e-09 | 31/47 (BT-474, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.737×** | -5.5 | 2e-06 | 24/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.748×** | -5.3 | 7e-06 | 24/48 (SW480, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.765×** | -4.6 | 2e-04 | 24/48 (HT-29, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -4.1 | 0.001 | 21/48 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.648×** | -4.1 | 0.001 | 25/48 (A-172, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.808×** | -3.9 | 0.004 | 17/48 (NCI-H2030, C32, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.826×** | -3.3 | 0.026 | 17/48 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Auranofin (drug)]] 0.5 µM |  | 0.835× | -3.2 | 0.035 | 11/48 (SW480, BT-474, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.043 | 16/48 (SNU-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.736×** | -2.9 | 0.081 | 14/48 (Panc 03.27, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.816×** | -2.8 | 0.092 | 11/48 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 78.3 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.299× (z -15.3) |
| [[A-427 (line)]] | wt | 81.0 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.329× (z -13.2) |
| [[KATO III (line)]] | alt | 68.1 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -20.6) |
| [[PANC-1 (line)]] | alt | 54.0 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -16.5) |
| [[LoVo (line)]] | wt | 36.2 | 2 (1 ⚠) | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +11.0) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.08× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 65.6 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -17.7) |
| [[SW480 (line)]] | alt | 57.6 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -14.5) |
| [[HT-29 (line)]] | alt | 45.3 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.230× (z -11.3) |
| [[A-172 (line)]] | wt | 102 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 72.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -14.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.343× (z -9.8) |
| [[AN3 CA (line)]] | alt | 135 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0516× (z -18.8) |
| [[C32 (line)]] | wt | 115 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.252× (z -11.0) |
| [[LS 180 (line)]] | wt | 35.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.9) ⚠ cell-cycle shift, explains ~10% of this change | [[Digitoxin (drug)]] 5 µM 0.201× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.307× (z -8.5) |
| [[C-33 A (line)]] | alt | 164 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.413× (z -10.4) |
| [[HOP62 (line)]] | alt | 71.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -14.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.216× (z -9.4) |
| [[HS-578T (line)]] | alt | 49.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 65.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -16.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.417× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 68.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 61.4 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.219× (z -9.8) |
| [[SNU-423 (line)]] | alt | 37.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.327× (z -9.1) |
| [[SW1417 (line)]] | alt | 26.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 102 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 37.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -11.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 75.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.612× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[LOX-IMVI (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -8.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H2030 (line)]] | alt | 58.5 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.185× (z -9.1) |
| [[RKO (line)]] | wt | 50.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.315× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SK-MEL-2 (line)]] | alt | 62.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.429× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 79.3 | 0 | 1 | — | [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM 0.0867× (z -8.7) |
| [[SW 900 (line)]] | alt | 62.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SW48 (line)]] | wt | 71.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.223× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 83.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 93.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF11]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ZNRF2P2]] | +0.61 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LSM6]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ATR]] | +0.59 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[DPY19L1P1]] | +0.59 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[PAXBP1]] | +0.58 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[SPECC1L]] | +0.57 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[CRTC3]] | +0.56 | +0.46 / +0.48 | both halves | 2e-05 | pathway: Organelle biogenesis and maintenance |
| [[RAB28]] | +0.56 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[NR2C2]] | +0.55 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[ATAD2B]] | +0.53 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[ZNRF2P1]] | +0.53 | +0.51 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATOSB]] | -0.51 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[MKNK1]] | -0.50 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[MYO7A]] | -0.49 | -0.40 / -0.45 | both halves | 4e-05 |  |
| [[MAPK8IP1]] | -0.49 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[ARF4-AS1]] | -0.49 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[KCTD10]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MYORG]] | -0.48 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[GNAI3]] | -0.48 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[FRG1JP]] | -0.48 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[HAPSTR1]] | -0.47 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[RAP1GAP]] | -0.47 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[RTF2]] | -0.46 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDGFL3]] | B | HDGFL3 activity raises PKD2's level | lines that do not express HDGFL3 (10) vs lines expressing it (40) | 1.79× lower at baseline in the lines without HDGFL3 | 0.089 | ⚠ within organs, on part of the lines; also absent: HLTF, GAMT, TIGD7 |
| [[ARHGAP27]] | B | ARHGAP27 activity lowers PKD2's level | lines that do not express ARHGAP27 (5) vs lines expressing it (45) | 1.40× higher at baseline in the lines without ARHGAP27 | 0.089 | ⚠ within organs, on part of the lines; also absent: TRIB3, LMNTD2, PLEKHN1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.416). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.8, 13.8); signed map (7.1, -4.7). **Vector** length 87.2, 22.5% of its response variance represented; |z| ≥ 3 in 1,059 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.6 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +4.8 | -5.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.9 | -8.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +4.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.5 | -10.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.9 | -14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | -4.1 | -3.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -7.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.8 | -1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | polycystin 2, transient receptor potential cation channel |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:88,007,635-88,077,777 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKD4, PC2, Pc-2, TRPP2 |
| Gene groups (HGNC) | EF-hand domain containing; Polycystin 2, transient receptor potential cation channel family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 5 pathways, smallest: VxPx cargo-targeting to cilium; Cargo trafficking to the periciliary membrane; Assembly of the 9+0 primary cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13563](https://www.uniprot.org/uniprotkb/Q13563) (Polycystin-2):

> Forms a nonselective cation channel. Can function as a homotetrameric ion channel or can form heteromer with PKD1. Displays distinct function depending on its subcellular localization and regulation by its binding partners. In primary cilium functions as a cation channel, with a preference for monovalent cations over divalent cations that allows K(+), Na(+) and Ca(2+) influx, with low selectivity for Ca(2+). Involved in fluid-flow mechanosensation by the primary cilium in renal epithelium (By …

**Summary**, from NCBI Gene [5311](https://www.ncbi.nlm.nih.gov/gene/5311):

> This gene encodes a member of the polycystin protein family. The encoded protein is a multi-pass membrane protein that functions as a calcium permeable cation channel, and is involved in calcium transport and calcium signaling in renal epithelial cells. This protein interacts with polycystin 1, and they may be partners in a common signaling cascade involved in tubular morphogenesis. Mutations in this gene are associated with autosomal dominant polycystic kidney disease type 2. [provided by …

**Accessions** — [HGNC:9009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9009) · Entrez [5311](https://www.ncbi.nlm.nih.gov/gene/5311) · UniProt [Q13563](https://www.uniprot.org/uniprotkb/Q13563) · Ensembl [ENSG00000118762](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118762)

## Data

Gene col 4016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4016); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4016]; `tensor/DDL_lfc|DDL_z.npy` [4016]; `embed/gene_vectors.npy` [4016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4016 or target_col == 4016). Every well: [[PKD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
