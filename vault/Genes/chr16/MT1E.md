---
symbol: "MT1E"
type: "gene"
col: 9842
ensembl_id: "ENSG00000169715"
name: "metallothionein 1E"
location: "16q13"
module: 113
arm: "+"
pooled_cpm: 58.94
n_lines_expressing: 28
n_dd_up: 23
n_dd_down: 13
n_dd_up_clean: 21
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 7
direction_downstream: 6
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# MT1E

*metallothionein 1E* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (2 with an alert ⚠); the strongest is [[Chlorhexidine (diacetate) (drug)]] 5 µM: 2.81× (z +9.4, q 4e-18, up in 24 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.332× (z -7.1, q 1e-09, down in 24 of 26 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.520× (z -5.9, q 1e-06, down in 23 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1M]] (+0.80, fdr 7e-06, ⚠ read-through risk), [[MT1X]] (+0.78, fdr 7e-06), [[MT2A]] (+0.78, fdr 7e-06, ⚠ read-through risk), [[IRX3]] (+0.75, fdr 7e-06), [[KLF9]] (+0.71, fdr 7e-06); moves opposite to [[ANXA10]] (-0.58, fdr 1e-05), [[SIRLNT]] (-0.53, fdr 5e-05), [[PGRMC1]] (-0.49, fdr 1e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 6 go from it, the strongest it → [[HPS5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9842.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **2.81×** | +9.4 | 4e-18 | 24/26 (SW480, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **2.25×** | +7.4 | 5e-11 | 15/26 (HOP62, SNU-423, …) | rises with dose | composition shift; position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **3.07×** | +7.2 | 1e-10 | 17/26 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.88×** | +6.8 | 1e-09 | 16/26 (NCI-H2347, SW 900, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.76×** | +6.3 | 4e-08 | 17/26 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.96×** | +6.1 | 9e-08 | 16/26 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **2.48×** | +5.8 | 5e-07 | 16/26 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.38×** | +5.6 | 2e-06 | 18/26 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **2.18×** | +5.0 | 3e-05 | 16/26 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **2.09×** | +4.7 | 1e-04 | 16/26 (NCI-H2347, SW 900, …) | all doses, flat | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.06×** | +4.7 | 2e-04 | 15/26 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **2.03×** | +4.6 | 2e-04 | 14/26 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.44×** | +4.4 | 4e-04 | 16/26 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +4.4 | 5e-04 | 17/26 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.96×** | +4.3 | 6e-04 | 15/26 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **1.95×** | +4.3 | 7e-04 | 16/26 (HOP62, NCI-H2347, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9842.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.332×** | -7.1 | 1e-09 | 24/26 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.520×** | -5.9 | 1e-06 | 23/26 (MIA PaCa-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.435×** | -5.3 | 2e-05 | 23/26 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.442×** | -4.9 | 1e-04 | 20/26 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.508×** | -4.3 | 0.002 | 18/26 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.314×** | -3.9 | 0.010 | 18/26 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.663×** | -3.7 | 0.017 | 17/26 (HT-29, RKO, …) | top dose only | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.570×** | -3.6 | 0.024 | 16/26 (RPMI-7951, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.347×** | -3.5 | 0.025 | 16/25 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.585×** | -3.4 | 0.035 | 19/25 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.690×** | -3.4 | 0.041 | 17/26 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.590×** | -3.2 | 0.056 | 18/26 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.595×** | -3.1 | 0.076 | 15/25 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.97 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9842. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 29.7 | 18 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 7.53× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 123 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.2× (z +20.8) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 9.96× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 105 | 6 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.84× (z +13.4) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 6.44× (z +9.2) | [[Ixazomib citrate (drug)]] 5 µM 0.0966× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.139× (z -9.7) |
| [[SNU-423 (line)]] | alt | 55.5 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +18.3) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.76× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 52.9 | 9 | 0 | [[Budesonide (drug)]] 0.5 µM 8.81× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 96.4 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.119× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.145× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 33.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +14.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.43× (z +8.8) | — |
| [[KATO III (line)]] | alt | 34.8 | 3 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.74× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 561 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -11.6) |
| [[SW480 (line)]] | alt | 51.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.87× (z +16.8) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 6.17× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 280 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +14.9) ⚠ cell-cycle shift, explains ~78% of this change | — |
| [[HepG2_C3A (line)]] | wt | 84.2 | 1 | 1 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.33× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.205× (z -9.6) |
| [[Hs 766T (line)]] | wt | 134 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +13.3) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 3.22× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 157 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.158× (z -9.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -8.6) |
| [[PANC-1 (line)]] | alt | 62.4 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.219× (z -9.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 132 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -10.4) |
| [[HCT15 (line)]] | alt | 57.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -8.6) |
| [[HT-29 (line)]] | alt | 19.6 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.46× (z +8.7) | — |
| [[LoVo (line)]] | wt | 67.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -8.8) |
| [[RKO (line)]] | wt | 106 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -8.7) |
| [[A-172 (line)]] | wt | 4.86 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.90 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.42 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.23 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.41 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 8.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.45 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.96 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.72 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.73 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 32.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9842), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1M]] | +0.80 | +0.81 / +0.81 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 853; ⚠ **readthrough risk**: MT1M lies 5.5 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[MT1X]] | +0.78 | +0.71 / +0.83 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 798 |
| [[MT2A]] | +0.78 | +0.70 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_HYPOXIA; STRING 829; ⚠ **readthrough risk**: this gene lies 16.0 kb 3′ of MT2A on the same strand (can correlate by spillover, not regulation) |
| [[MT1F]] | +0.76 | +0.76 / +0.72 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 797; ⚠ same locus (30.6 kb, same strand: neighbours can correlate without regulation) |
| [[IRX3]] | +0.75 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[MT1A]] | +0.71 | +0.59 / +0.70 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 479; ⚠ **readthrough risk**: MT1A lies 11.6 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[KLF9]] | +0.71 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ZMYND8]] | +0.71 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[IRS2]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[SAA1]] | +0.68 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[ARL4A]] | +0.67 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[CEBPB]] | +0.66 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[TSC22D3]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TLR2]] | +0.65 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[CCL20]] | +0.64 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[FOXC2]] | +0.64 | +0.57 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA10]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[SIRLNT]] | -0.53 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[PGRMC1]] | -0.49 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[IL18BP]] | -0.48 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[BBOX1-AS1]] | -0.48 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MLLT11]] | -0.48 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[E2F7]] | -0.47 | -0.50 / -0.38 | both halves | 7e-05 |  |
| [[RABGEF1P3]] | -0.47 | -0.43 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises MT1E's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.6% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[CCBE1]] | B | CCBE1 activity raises MT1E's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without CCBE1 | 0.079 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[PTX3]] | B | PTX3 activity raises MT1E's level | lines that do not express PTX3 (24) vs lines expressing it (26) | 1.91× lower at baseline in the lines without PTX3 | 0.080 | ⚠ within organs, on part of the lines; also absent: IL7R, RNF182, COL5A1 |
| [[TOP2A]] | B | TOP2A activity raises MT1E's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MT1M]] | C | MT1M activity raises MT1E's level | lines that do not express MT1M (29) vs lines expressing it (21) | 4.35× lower at baseline in the lines without MT1M | 0.002 | ⚠ within organs, on part of the lines; also absent: IRAK3, MIR155HG, G0S2; co-absent with the target |
| [[MT1A]] | C | MT1A activity raises MT1E's level | lines that do not express MT1A (33) vs lines expressing it (17) | 3.12× lower at baseline in the lines without MT1A | 0.042 | ⚠ within organs, on part of the lines; also absent: WT1-AS, KRT5, ENSG00000238178; co-absent with the target |
| [[MT1G]] | C | MT1G activity raises MT1E's level | lines that do not express MT1G (31) vs lines expressing it (19) | 4.04× lower at baseline in the lines without MT1G | 0.085 | ⚠ within organs, on part of the lines; also absent: TFF2, PROM1, FOXQ1; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HPS5]] | B | MT1E activity lowers HPS5's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.41× higher at baseline in the lines without MT1E | 0.006 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5 |
| [[CCBE1]] | B | MT1E activity raises CCBE1's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without MT1E | 0.036 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5 |
| [[FHL3]] | B | MT1E activity raises FHL3's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.41× lower at baseline in the lines without MT1E | 0.073 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5 |
| [[PTX3]] | B | MT1E activity raises PTX3's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.40× lower at baseline in the lines without MT1E | 0.096 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5 |
| [[MT1M]] | C | MT1E activity raises MT1M's level | lines that do not express MT1E (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without MT1E | 0.032 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5; co-absent with the target |
| [[IRAK3]] | C | MT1E activity raises IRAK3's level | lines that do not express MT1E (22) vs lines expressing it (28) | 2.82× lower at baseline in the lines without MT1E | 0.083 | ⚠ within organs, on part of the lines; also absent: MT1M, ENSG00000291105, ACSL5; co-absent with the target |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.796). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.1, 13.4); signed map (14.6, 31.1). **Vector** length 93.1, 27.7% of its response variance represented; |z| ≥ 3 in 794 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.53 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +6.0 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +4.5 | +2.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.5 | +6.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +4.2 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +4.2 | +5.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +4.2 | +5.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +4.1 | +4.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.8 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.6 | -4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.5 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | metallothionein 1E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,625,475-56,627,112 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MTD; previously MT1 |
| Gene groups (HGNC) | Metallothioneins |
| Hallmark sets | UV_RESPONSE_DN, HYPOXIA |
| Reactome | 3 pathways, smallest: Metallothioneins bind metals; Response to metal ions; Cellular responses to stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [P04732](https://www.uniprot.org/uniprotkb/P04732) (Metallothionein-1E):

> Metallothioneins have a high content of cysteine residues that bind various heavy metals; these proteins are transcriptionally regulated by both heavy metals and glucocorticoids.

**Summary**, from NCBI Gene [4493](https://www.ncbi.nlm.nih.gov/gene/4493):

> Predicted to enable zinc ion binding activity. Involved in cellular response to cadmium ion and cellular response to zinc ion. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7397](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7397) · Entrez [4493](https://www.ncbi.nlm.nih.gov/gene/4493) · UniProt [P04732](https://www.uniprot.org/uniprotkb/P04732) · Ensembl [ENSG00000169715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169715)

## Data

Gene col 9842: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9842); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9842, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9842]; `tensor/DDL_lfc|DDL_z.npy` [9842]; `embed/gene_vectors.npy` [9842]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9842 or target_col == 9842). Every well: [[MT1E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT1E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
