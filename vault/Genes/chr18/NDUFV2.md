---
symbol: "NDUFV2"
type: "gene"
col: 10900
ensembl_id: "ENSG00000178127"
name: "NADH:ubiquinone oxidoreductase core subunit V2"
location: "18p11.22"
module: 65
arm: "+"
pooled_cpm: 126.75
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 16
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# NDUFV2

*NADH:ubiquinone oxidoreductase core subunit V2* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.30× (z +5.4, q 4e-05, up in 29 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.30× (z +5.3, q 4e-05, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.603× (z -14.4, q 4e-44, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRMT9]] (+0.68, fdr 7e-06), [[PEX2]] (+0.66, fdr 7e-06), [[CASC3]] (+0.64, fdr 9e-06); moves opposite to [[GATAD2A]] (-0.61, fdr 2e-05), [[KPNA4]] (-0.60, fdr 1e-05), [[STK10]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +5.4 | 4e-05 | 29/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +5.3 | 4e-05 | 30/48 (LoVo, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +4.9 | 2e-04 | 24/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 9e-04 | 23/47 (A-172, RKO, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +4.2 | 0.003 | 23/48 (BT-474, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.15× | +4.1 | 0.004 | 17/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.012 | 22/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.6 | 0.025 | 15/38 (A-427, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.19× | +3.4 | 0.037 | 19/47 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.3 | 0.048 | 3/48 (SHP-77, SW 900, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.10 | 18/49 (NCI-H23, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -14.4 | 4e-44 | 47/49 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.635×** | -9.1 | 2e-17 | 38/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.662×** | -8.3 | 2e-14 | 39/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.675×** | -7.6 | 5e-12 | 30/44 (C-33 A, BT-474, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.797×** | -6.4 | 2e-08 | 30/48 (A-427, SNU-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.739×** | -6.1 | 1e-07 | 34/48 (NCI-H460, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.756×** | -5.6 | 2e-06 | 31/48 (SW480, SW48, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.754×** | -5.4 | 4e-06 | 30/50 (SW480, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.758×** | -5.3 | 6e-06 | 30/48 (NCI-H460, SW480, …) | top dose only |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.805×** | -4.3 | 8e-04 | 24/48 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.805×** | -4.3 | 8e-04 | 24/48 (HOP62, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.809×** | -4.2 | 0.001 | 24/48 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.811×** | -4.2 | 0.001 | 22/48 (HOP62, LS 180, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.822×** | -3.9 | 0.003 | 21/49 (SNU-1, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.819×** | -3.8 | 0.004 | 21/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.827×** | -3.7 | 0.009 | 17/48 (HOP62, RPMI-7951, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.840× | -3.5 | 0.017 | 17/48 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.842× | -3.4 | 0.019 | 16/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.846× | -3.3 | 0.025 | 19/49 (SW 1088, SW1417, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.853× | -3.2 | 0.040 | 16/49 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.853× | -3.0 | 0.058 | 13/48 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.859× | -3.0 | 0.058 | 9/48 (HOP62, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 235 | 5 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.35× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.266× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 144 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -18.1) |
| [[LoVo (line)]] | wt | 114 | 3 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.18× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.458× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 320 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -19.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -12.3) |
| [[SW480 (line)]] | alt | 152 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -16.6) |
| [[A-427 (line)]] | wt | 525 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.581× (z -11.2) |
| [[A549 (line)]] | wt | 112 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -15.7) |
| [[COLO 205 (line)]] | alt | 127 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -11.5) |
| [[HOP62 (line)]] | alt | 169 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -8.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -8.6) |
| [[HT-29 (line)]] | alt | 148 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -11.6) |
| [[KATO III (line)]] | alt | 110 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.01× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -10.7) |
| [[NCI-H2347 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -8.6) |
| [[C-33 A (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0942× (z -21.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 82.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 81.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 134 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -8.5) |
| [[LS 180 (line)]] | wt | 112 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 89.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 160 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 99.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -12.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -8.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 79.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.5) |
| [[RKO (line)]] | wt | 114 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -12.1) |
| [[SNU-1 (line)]] | wt | 154 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -10.8) |
| [[SW 1271 (line)]] | alt | 61.7 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0948× (z -9.2) |
| [[SW48 (line)]] | wt | 134 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.414× (z -8.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 75.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 62.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 92.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 149 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 157 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 83.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 109 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRMT9]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[PEX2]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[CASC3]] | +0.64 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[MTX2]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 465 |
| [[MRPL39]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[FIP1L1]] | +0.61 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[AUH]] | +0.61 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[TSNAX]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[CMC1]] | +0.58 | +0.63 / +0.51 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[MAP3K2]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MBIP]] | +0.58 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.58 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.61 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[KPNA4]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[STK10]] | -0.56 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[SETX]] | -0.55 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[KCTD5]] | -0.53 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[GPATCH2L]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SAP30BP]] | -0.53 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[ZNF469]] | -0.53 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[HCG18]] | -0.52 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[DMPK]] | -0.51 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ZDHHC11]] | -0.51 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CRK]] | -0.50 | -0.44 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NDUFV2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.683). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-5.4, -9.8); signed map (-29.5, -13.4). **Vector** length 111, 32.3% of its response variance represented; |z| ≥ 3 in 1,005 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.9 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | -0.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +1.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.4 | +1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.0 | +1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.6 | -6.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.8 | -4.2 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -2.7 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase core subunit V2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.22 — chr18:9,102,630-9,134,345 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CI-24k |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P19404](https://www.uniprot.org/uniprotkb/P19404) (NADH dehydrogenase):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor (Probable). Parts of the peripheral arm of the enzyme, where the electrons from NADH are accepted by flavin mononucleotide (FMN) and then passed along a chain of iron-sulfur clusters by electron tunnelling to the final acceptor ubiquinone (Probable). Contains one iron-sulfur cluster …

**Summary**, from NCBI Gene [4729](https://www.ncbi.nlm.nih.gov/gene/4729):

> The NADH-ubiquinone oxidoreductase complex (complex I) of the mitochondrial respiratory chain catalyzes the transfer of electrons from NADH to ubiquinone, and consists of at least 43 subunits. The complex is located in the inner mitochondrial membrane. This gene encodes the 24 kDa subunit of complex I, and is involved in electron transfer. Mutations in this gene are implicated in Parkinson's disease, bipolar disorder, schizophrenia, and have been found in one case of early onset hypertrophic …

**Accessions** — [HGNC:7717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7717) · Entrez [4729](https://www.ncbi.nlm.nih.gov/gene/4729) · UniProt [P19404](https://www.uniprot.org/uniprotkb/P19404) · Ensembl [ENSG00000178127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178127)

## Data

Gene col 10900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10900); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10900]; `tensor/DDL_lfc|DDL_z.npy` [10900]; `embed/gene_vectors.npy` [10900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10900 or target_col == 10900). Every well: [[NDUFV2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFV2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
