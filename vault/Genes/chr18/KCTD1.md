---
symbol: "KCTD1"
type: "gene"
col: 5569
ensembl_id: "ENSG00000134504"
name: "potassium channel tetramerization domain containing 1"
location: "18q11.2"
module: 15
arm: "+"
pooled_cpm: 26.43
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# KCTD1

*potassium channel tetramerization domain containing 1* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +16.2, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.488× (z -17.2, q 0e+00, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANXA2R-OT1]] (+0.67, fdr 5e-05), [[PTGR3]] (+0.62, fdr 3e-05), [[TRIM7]] (+0.61, fdr 1e-04); moves opposite to [[DDX19B]] (-0.55, fdr 7e-05), [[ASL]] (-0.51, fdr 0.001, ⚠ not reproduced), [[RALGAPA2]] (-0.50, fdr 5e-04), [[NBEAL1]] (-0.48, fdr 6e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5569.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +16.2 | 0e+00 | 44/47 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.8 | 2e-20 | 36/46 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +7.1 | 2e-10 | 28/48 (A-172, A-427, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.2 | 2e-05 | 24/48 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +4.1 | 0.005 | 12/48 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.9 | 0.009 | 16/47 (HS-578T, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.25×** | +3.8 | 0.012 | 15/48 (LS 180, NCI-H1792, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.029 | 10/48 (NCI-H1792, KATO III, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~14% of this change | **1.24×** | +3.5 | 0.029 | 17/43 (SW1417, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.029 | 13/48 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.15× | +3.4 | 0.032 | 9/48 (CFPAC-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5569.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.488×** | -17.2 | 0e+00 | 35/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.587×** | -9.0 | 4e-17 | 32/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -8.1 | 1e-13 | 28/46 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.634×** | -7.7 | 1e-12 | 27/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.624×** | -7.7 | 2e-12 | 27/47 (NCI-H460, A-172, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.639×** | -7.6 | 3e-12 | 24/47 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -7.0 | 2e-10 | 26/47 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.697×** | -6.1 | 6e-08 | 26/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.698×** | -6.1 | 6e-08 | 23/48 (A549, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -5.7 | 7e-07 | 25/47 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.721×** | -5.2 | 8e-06 | 22/47 (A498, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.588×** | -4.7 | 1e-04 | 19/48 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.761×** | -4.6 | 2e-04 | 20/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.764×** | -4.6 | 2e-04 | 21/47 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.771×** | -4.2 | 9e-04 | 21/46 (J82, RKO, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.728×** | -3.8 | 0.004 | 11/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.671×** | -3.5 | 0.013 | 8/47 (LOX-IMVI, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.678×** | -3.5 | 0.017 | 12/45 (HEC-1-A, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.683×** | -3.4 | 0.021 | 15/45 (BT-474, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.870× | -3.3 | 0.023 | 12/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5569. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.4 | 1 | 12 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -21.7) |
| [[A498 (line)]] | wt | 35.0 | 2 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -14.5) |
| [[A-172 (line)]] | wt | 25.4 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -17.3) |
| [[LOX-IMVI (line)]] | wt | 37.5 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.1) |
| [[A549 (line)]] | wt | 52.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.218× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 67.2 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.214× (z -11.1) |
| [[H4 (line)]] | wt | 33.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 48.1 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.361× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 28.2 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.1) |
| [[C32 (line)]] | wt | 38.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -18.2) |
| [[HS-578T (line)]] | alt | 27.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.6) |
| [[LS 180 (line)]] | wt | 25.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.43× (z +15.6) | — |
| [[LoVo (line)]] | wt | 30.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 30.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.1) |
| [[PANC-1 (line)]] | alt | 29.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -18.4) |
| [[RKO (line)]] | wt | 19.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +11.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 10.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.0) | [[Bendamustine (drug)]] 5 µM 0.187× (z -8.6) |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0854× (z -8.5) |
| [[BT-474 (line)]] | alt | 60.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.7) |
| [[HOP62 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -8.9) |
| [[Hs 766T (line)]] | wt | 33.3 | 0 | 1 | — | [[venetoclax (drug)]] 5 µM 0.0672× (z -9.5) |
| [[J82 (line)]] | alt | 13.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0683× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 52.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -16.9) |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0868× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -9.1) |
| [[SW48 (line)]] | wt | 39.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.5) | — |
| [[SW480 (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +8.8) | — |
| [[A-427 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5569), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANXA2R-OT1]] | +0.67 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[PTGR3]] | +0.62 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[TRIM7]] | +0.61 | +0.33 / +0.53 | both halves | 1e-04 |  |
| [[RNF217-AS1]] | +0.60 | +0.36 / +0.39 | both halves | 1e-04 |  |
| [[HOXB-AS1]] | +0.59 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[SEC24B-AS1]] | +0.59 | +0.41 / +0.34 | both halves | 1e-04 |  |
| [[SETD1B]] | +0.59 | +0.45 / +0.34 | both halves | 1e-04 |  |
| [[KLHL42]] | +0.57 | +0.43 / +0.28 | both halves | 3e-04 | same gene group |
| [[SAP30L-AS1]] | +0.57 | +0.45 / +0.30 | both halves | 2e-04 |  |
| [[CDK2AP1]] | +0.57 | +0.41 / +0.31 | both halves | 2e-04 |  |
| [[HOXB7]] | +0.56 | +0.27 / +0.39 | both halves | 3e-04 |  |
| [[ANGEL2]] | +0.56 | +0.36 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX19B]] | -0.55 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[ASL]] | -0.51 | -0.42 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[RALGAPA2]] | -0.50 | -0.23 / -0.29 | both halves | 5e-04 |  |
| [[FCHO1]] | -0.48 | -0.36 / -0.08 | ⚠ not reproduced | 0.003 |  |
| [[NBEAL1]] | -0.48 | -0.36 / -0.21 | both halves | 6e-04 |  |
| [[HIF1AN]] | -0.48 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[SLC45A4]] | -0.47 | -0.42 / -0.23 | both halves | 5e-04 |  |
| [[TBC1D10A]] | -0.47 | -0.39 / -0.20 | ⚠ not reproduced | 8e-04 |  |
| [[PRKCI]] | -0.47 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[TTC1]] | -0.47 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[MIR3667HG]] | -0.46 | -0.40 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCTD1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLCL2]] | B | PLCL2 activity raises KCTD1's level | lines that do not express PLCL2 (12) vs lines expressing it (38) | 1.53× lower at baseline in the lines without PLCL2 | 0.056 | ⚠ within organs, on part of the lines |
| [[TOP2B]] | B | TOP2B activity lowers KCTD1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[VAX2]] | B | VAX2 activity lowers KCTD1's level | lines that do not express VAX2 (12) vs lines expressing it (38) | 1.01× higher at baseline in the lines without VAX2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with RNF43; also absent: ZNF512B, WHAMMP2, HLTF |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.3, 20.3); signed map (17.7, -5.6). **Vector** length 84.1, 17.6% of its response variance represented; |z| ≥ 3 in 1,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +16.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.8 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +1.7 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.8 | -6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -17.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | -2.6 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | potassium channel tetramerization domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:26,454,910-26,657,401 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C18orf5 |
| Gene groups (HGNC) | BTB domain containing; MicroRNA protein coding host genes; KCTD family |
| Reactome | 2 pathways, smallest: Negative regulation of activity of TFAP2 (AP-2) family transcription factors; Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q719H9](https://www.uniprot.org/uniprotkb/Q719H9) (BTB/POZ domain-containing protein KCTD1):

> Is a regulator of different signaling pathways. Up-regulates ADCY5 thereby enhancing cAMP signaling, and is involved in the negative regulation of Wnt canonical, Hh and Notch signaling. Is a repressor of transcriptional activation mediated by AP-2 family members, including TFAP2A, TFAP2B and TFAP2C to various extent.

**Summary**, from NCBI Gene [284252](https://www.ncbi.nlm.nih.gov/gene/284252):

> This gene encodes a protein containing a BTB (Broad-complex, tramtrack and bric a brac), also known as a POZ (POxvirus and zinc finger) protein-protein interaction domain. The encoded protein negatively regulates the AP-2 family of transcription factors and the Wnt signaling pathway. A mechanism for the modulation of Wnt signaling has been proposed in which the encoded protein enhances ubiquitination and degradation of the beta-catenin protein. Mutations in this gene have been identified in …

**Accessions** — [HGNC:18249](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18249) · Entrez [284252](https://www.ncbi.nlm.nih.gov/gene/284252) · UniProt [Q719H9](https://www.uniprot.org/uniprotkb/Q719H9) · Ensembl [ENSG00000134504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134504)

## Data

Gene col 5569: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5569); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5569, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5569]; `tensor/DDL_lfc|DDL_z.npy` [5569]; `embed/gene_vectors.npy` [5569]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5569 or target_col == 5569). Every well: [[KCTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
