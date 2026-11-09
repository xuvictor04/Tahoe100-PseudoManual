---
symbol: "FER1L4"
type: "gene"
col: 1529
ensembl_id: "ENSG00000088340"
name: "fer-1 like family member 4 (pseudogene)"
location: "20q11.22"
module: 47
arm: "+"
pooled_cpm: 33.33
n_lines_expressing: 43
n_dd_up: 8
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 8
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# FER1L4

*fer-1 like family member 4 (pseudogene)* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.49× (z +7.2, q 4e-10, up in 19 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.364× (z -12.3, q 9e-32, down in 32 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.489× (z -9.0, q 4e-17, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOTCH3]] (+0.63, fdr 1e-05), [[PIP5KL1]] (+0.62, fdr 7e-06), [[UCKL1-AS1]] (+0.60, fdr 1e-05); moves opposite to [[MTX2]] (-0.60, fdr 9e-06), [[VRK2]] (-0.51, fdr 2e-05), [[NIPSNAP2]] (-0.51, fdr 3e-05).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 8 go from it, the strongest it → [[MIR22HG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +7.2 | 4e-10 | 19/40 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +6.8 | 3e-09 | 22/41 (RKO, SW480, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +6.7 | 3e-09 | 23/41 (NCI-H1573, SW480, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.47×** | +4.9 | 2e-04 | 22/41 (A-427, NCI-H1792, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.021 | 15/40 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.036 | 13/41 (SW480, NCI-H2030, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.076 | 16/41 (HOP62, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.078 | 15/41 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 0.05 µM |  | 1.31× | +3.1 | 0.11 | 10/40 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 1.28× | +3.1 | 0.11 | 8/41 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 1.58× | +3.0 | 0.12 | 9/39 (NCI-H1792, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1529.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.364×** | -12.3 | 9e-32 | 32/40 (KATO III, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.480×** | -9.2 | 8e-18 | 29/39 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.489×** | -9.0 | 4e-17 | 26/41 (RPMI-7951, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.462×** | -8.9 | 9e-17 | 31/41 (RPMI-7951, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.481×** | -8.9 | 9e-17 | 27/37 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.484×** | -8.8 | 1e-16 | 27/40 (RPMI-7951, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -8.3 | 7e-15 | 28/41 (RPMI-7951, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.593×** | -6.6 | 3e-09 | 27/40 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.716×** | -5.9 | 2e-07 | 23/41 (J82, RPMI-7951, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.656×** | -5.3 | 6e-06 | 27/41 (HT-29, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.675×** | -4.9 | 6e-05 | 23/41 (SW 1088, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.660×** | -4.8 | 6e-05 | 20/33 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.688×** | -4.7 | 1e-04 | 22/41 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.722×** | -4.1 | 0.002 | 20/41 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -3.6 | 0.010 | 15/40 (J82, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.826×** | -3.4 | 0.022 | 15/41 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -3.2 | 0.048 | 13/41 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.777×** | -3.1 | 0.051 | 11/40 (KATO III, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[EX229 (drug)]] 5 µM |  | **0.625×** | -3.1 | 0.053 | 11/41 (MIA PaCa-2, HT-29, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0320× (z -23.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -16.4) |
| [[BT-474 (line)]] | alt | 41.9 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0594× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.152× (z -16.0) |
| [[KATO III (line)]] | alt | 36.7 | 0 | 7 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0578× (z -18.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.155× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 59.4 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +12.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -15.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.195× (z -12.2) |
| [[Hs 766T (line)]] | wt | 30.1 | 0 | 4 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0690× (z -12.9) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.150× (z -9.1) |
| [[J82 (line)]] | alt | 73.8 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.266× (z -12.9) |
| [[LS 180 (line)]] | wt | 21.5 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.160× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 14.9 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +18.0) | [[Harringtonine (drug)]] 5 µM 0.292× (z -9.0) |
| [[SW480 (line)]] | alt | 14.3 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +13.7) | [[Harringtonine (drug)]] 5 µM 0.288× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 26.5 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +10.7) | [[Digitoxin (drug)]] 0.5 µM 0.165× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 59.7 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.111× (z -14.8) ⚠ toxic |
| [[A498 (line)]] | wt | 21.5 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.27× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 70.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -12.9) ⚠ toxic |
| [[HOP62 (line)]] | alt | 79.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.187× (z -10.5) ⚠ toxic |
| [[HS-578T (line)]] | alt | 35.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +9.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -9.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 160 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.2) |
| [[LoVo (line)]] | wt | 10.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.2× (z +20.7) | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.223× (z -9.1) |
| [[RKO (line)]] | wt | 19.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.92× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -10.2) ⚠ cell-cycle shift, explains ~17% of this change |
| [[SNU-423 (line)]] | alt | 54.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -9.5) ⚠ cell-cycle shift, explains ~17% of this change |
| [[A549 (line)]] | wt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -8.8) |
| [[HCT15 (line)]] | alt | 52.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 9.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.36× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 33.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.319× (z -8.6) |
| [[SW48 (line)]] | wt | 8.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.49× (z +9.4) | — |
| [[A-172 (line)]] | wt | 4.03 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.21 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.00 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.84 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH3]] | +0.63 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[PIP5KL1]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[UCKL1-AS1]] | +0.60 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[PITRM1-AS1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[EPHA1-AS1]] | +0.58 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[INTS6]] | +0.58 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SEMA4A]] | +0.57 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[DNAH1]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SLC8A2]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[LRRC23]] | +0.56 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.56 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SFXN5]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTX2]] | -0.60 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[VRK2]] | -0.51 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NIPSNAP2]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[LRIG2]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[NEK3]] | -0.50 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[UBXN2B]] | -0.50 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[PAIP1]] | -0.50 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[PYURF]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[SYPL1]] | -0.49 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[VPS36]] | -0.49 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[GNPTAB]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ARMC1]] | -0.49 | -0.33 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR22HG]] | B | FER1L4 activity raises MIR22HG's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without FER1L4 | 0.041 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[PITRM1-AS1]] | B | FER1L4 activity raises PITRM1-AS1's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without FER1L4 | 0.049 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[AP1G1]] | B | FER1L4 activity raises AP1G1's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.26× lower at baseline in the lines without FER1L4 | 0.049 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[ZSWIM6]] | B | FER1L4 activity raises ZSWIM6's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.41× lower at baseline in the lines without FER1L4 | 0.050 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[INTS6]] | B | FER1L4 activity raises INTS6's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without FER1L4 | 0.051 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | B | FER1L4 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express FER1L4 (7) vs lines expressing it (41) | the lines without FER1L4: 0.88× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[LINC00672]] | B | FER1L4 activity raises LINC00672's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.35× lower at baseline in the lines without FER1L4 | 0.075 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[SLC9A5]] | B | FER1L4 activity raises SLC9A5's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.27× lower at baseline in the lines without FER1L4 | 0.093 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (39.3, -20.1); signed map (14.8, 15.2). **Vector** length 107, 27.6% of its response variance represented; |z| ≥ 3 in 1,164 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.7 | +6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.5 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +1.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.7 | -8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -8.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -12.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -4.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.8 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | fer-1 like family member 4 (pseudogene) |
| Locus type | pseudogene |
| Location | 20q11.22 — chr20:35,558,866-35,607,494 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | FER1L4P, bA563A22B.1, dJ309K20.1; previously C20orf124 |
| Gene groups (HGNC) | Ferlin family; Unitary pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [80307](https://www.ncbi.nlm.nih.gov/gene/80307):

> Predicted to enable metal ion binding activity. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15801) · Entrez [80307](https://www.ncbi.nlm.nih.gov/gene/80307) · Ensembl [ENSG00000088340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088340)

## Data

Gene col 1529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1529); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1529]; `tensor/DDL_lfc|DDL_z.npy` [1529]; `embed/gene_vectors.npy` [1529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1529 or target_col == 1529). Every well: [[FER1L4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FER1L4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
