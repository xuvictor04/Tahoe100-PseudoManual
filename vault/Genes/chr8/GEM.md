---
symbol: "GEM"
type: "gene"
col: 9040
ensembl_id: "ENSG00000164949"
name: "GTP binding protein overexpressed in skeletal muscle"
location: "8q22.1"
module: 112
arm: "+"
pooled_cpm: 33.8
n_lines_expressing: 41
n_dd_up: 36
n_dd_down: 17
n_dd_up_clean: 29
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 16
direction_downstream: 18
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# GEM

*GTP binding protein overexpressed in skeletal muscle* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.96× (z +22.2, q 0e+00, up in 36 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.578× (z -5.6, q 1e-05, down in 22 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP10]] (+0.77, fdr 7e-06), [[IER3]] (+0.71, fdr 7e-06), [[BHLHE40]] (+0.64, fdr 2e-05); moves opposite to [[ARMC8]] (-0.56, fdr 1e-05), [[C8orf76]] (-0.50, fdr 3e-05), [[EIF4ENIF1]] (-0.49, fdr 5e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[C6orf141]] → it (grade B ⚠); 18 go from it, the strongest it → [[MAFK]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9040.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.96×** | +22.2 | 0e+00 | 36/38 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.98×** | +19.6 | 0e+00 | 37/38 (HS-578T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.37×** | +16.8 | 0e+00 | 35/38 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.59×** | +14.6 | 0e+00 | 36/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **7.43×** | +12.0 | 7e-31 | 37/40 (LoVo, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +11.8 | 2e-30 | 35/38 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.98×** | +11.3 | 8e-28 | 35/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.63×** | +11.0 | 2e-26 | 30/38 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.60×** | +10.5 | 6e-24 | 33/37 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.52×** | +9.6 | 7e-20 | 33/39 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.73×** | +8.8 | 5e-17 | 34/39 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +8.3 | 4e-15 | 27/39 (A-172, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.00×** | +7.9 | 9e-14 | 29/39 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.74×** | +7.9 | 1e-13 | 27/38 (hTERT-HPNE, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **2.00×** | +7.7 | 6e-13 | 27/39 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +6.6 | 1e-09 | 22/39 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +5.7 | 5e-07 | 25/39 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9040.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.578×** | -5.6 | 1e-05 | 22/39 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.865× | -5.5 | 1e-05 | 12/40 (NCI-H23, LS 180, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.624×** | -5.4 | 2e-05 | 23/39 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.625×** | -5.2 | 3e-05 | 23/38 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.608×** | -5.1 | 3e-05 | 18/39 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.730×** | -5.0 | 5e-05 | 19/39 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **0.631×** | -4.7 | 1e-04 | 20/39 (HOP62, NCI-H1573, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.744×** | -4.7 | 1e-04 | 20/38 (SW48, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.659×** | -4.7 | 1e-04 | 21/39 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.671×** | -4.5 | 4e-04 | 17/39 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.676×** | -4.3 | 9e-04 | 22/39 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -4.2 | 0.001 | 22/38 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.694×** | -3.8 | 0.006 | 15/38 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.717×** | -3.8 | 0.007 | 19/39 (NCI-H1573, SNU-423, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.725×** | -3.6 | 0.010 | 18/38 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -3.5 | 0.018 | 19/40 (SNU-423, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9040. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 66.1 | 9 (2 ⚠) | 14 | [[Harringtonine (drug)]] 5 µM 14.1× (z +17.4) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.161× (z -12.6) |
| [[HOP62 (line)]] | alt | 82.3 | 6 | 10 | [[Harringtonine (drug)]] 5 µM 6.85× (z +12.1) | [[Clobetasol propionate (drug)]] 0.05 µM 0.183× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 11.8 | 13 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 27.0× (z +19.9) | — |
| [[AsPC-1 (line)]] | alt | 58.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.0× (z +25.3) | — |
| [[NCI-H2347 (line)]] | alt | 75.2 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.72× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 106 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +17.6) | — |
| [[LOX-IMVI (line)]] | wt | 25.5 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.58× (z +18.1) | — |
| [[SNU-423 (line)]] | alt | 96.4 | 3 | 3 | [[Harringtonine (drug)]] 5 µM 5.14× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -12.7) |
| [[HS-578T (line)]] | alt | 65.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +21.9) | — |
| [[A-172 (line)]] | wt | 16.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +17.8) | — |
| [[A498 (line)]] | wt | 68.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +21.9) | — |
| [[A549 (line)]] | wt | 28.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.35× (z +15.4) | — |
| [[KATO III (line)]] | alt | 29.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +11.0) | — |
| [[LoVo (line)]] | wt | 46.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +16.4) | — |
| [[NCI-H1792 (line)]] | alt | 42.3 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 8.87× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.71× (z +10.7) | — |
| [[PANC-1 (line)]] | alt | 15.1 | 3 | 1 | [[Harringtonine (drug)]] 5 µM 7.03× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -8.7) |
| [[SW48 (line)]] | wt | 71.7 | 3 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 7.19× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.87× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -14.0) |
| [[COLO 205 (line)]] | alt | 28.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +16.1) | — |
| [[Hs 766T (line)]] | wt | 17.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +12.0) | — |
| [[J82 (line)]] | alt | 12.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +15.5) | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +15.8) | — |
| [[SK-MEL-2 (line)]] | alt | 15.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +12.2) | — |
| [[SW 900 (line)]] | alt | 64.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +12.3) | — |
| [[SW1417 (line)]] | alt | 12.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +13.9) | — |
| [[CFPAC-1 (line)]] | alt | 32.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.77× (z +17.1) | — |
| [[LS 180 (line)]] | wt | 69.7 | 2 | 0 | [[Selinexor (drug)]] 5 µM 2.32× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 82.5 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 5.98× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -8.6) |
| [[HT-29 (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.479× (z -10.2) ⚠ position not correctable |
| [[RKO (line)]] | wt | 63.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -11.5) |
| [[SHP-77 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 7.82× (z +11.6) ⚠ toxic | — |
| [[A-427 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.85 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.20 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.83 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9040), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP10]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[IER3]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BHLHE40]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CXCL8]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[LINC02154]] | +0.64 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[KIAA1217]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CRYM]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[INHBA]] | +0.60 | +0.59 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[ROR1-AS1]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[NPTX1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CDKN2B]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[CSRNP1]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMC8]] | -0.56 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[C8orf76]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[EIF4ENIF1]] | -0.49 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[UBP1]] | -0.49 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[TRAPPC10]] | -0.49 | -0.34 / -0.57 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C6orf141]] | B | C6orf141 activity raises GEM's level | lines that do not express C6orf141 (21) vs lines expressing it (29) | 2.80× lower at baseline in the lines without C6orf141 | 0.004 | ⚠ within organs, on part of the lines; also absent: ADAM8, ENSG00000251584, SAMD12-AS1 |
| [[CXCL8]] | B | CXCL8 activity raises GEM's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without CXCL8 | 0.010 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |
| [[IL1A]] | B | IL1A activity raises GEM's level | lines that do not express IL1A (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without IL1A | 0.013 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[MIR155HG]] | B | MIR155HG activity raises GEM's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without MIR155HG | 0.025 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[NR3C1]] | B | NR3C1 activity lowers GEM's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[FAM107B]] | B | FAM107B activity raises GEM's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.66× lower at baseline in the lines without FAM107B | 0.045 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[PTGS2]] | B | PTGS2 activity raises GEM's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without PTGS2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[CSF2]] | B | CSF2 activity raises GEM's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without CSF2 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[DUSP10]] | B | DUSP10 activity raises GEM's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.44× lower at baseline in the lines without DUSP10 | 0.061 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[NFATC2]] | B | NFATC2 activity strengthens GEM's drug response | lines that do not express NFATC2 (8) vs lines expressing it (32) | the lines without NFATC2 respond 0.60× as strongly (z diff +2.15); strongest at Homoharringtonine 0.5 µM: 1.94x vs 4.85x (z diff +3.7) | 0.066 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[IL6]] | B | IL6 activity raises GEM's level | lines that do not express IL6 (32) vs lines expressing it (18) | 2.27× lower at baseline in the lines without IL6 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[TOP2A]] | B | TOP2A activity raises GEM's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAFK]] | B | GEM activity raises MAFK's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without GEM | 0.010 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[C6orf141]] | B | GEM activity raises C6orf141's level | lines that do not express GEM (9) vs lines expressing it (41) | 3.60× lower at baseline in the lines without GEM | 0.012 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[NFKBIZ]] | B | GEM activity raises NFKBIZ's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.24× lower at baseline in the lines without GEM | 0.012 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[IER3]] | B | GEM activity raises IER3's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.73× lower at baseline in the lines without GEM | 0.012 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[DUSP10]] | B | GEM activity raises DUSP10's level | lines that do not express GEM (9) vs lines expressing it (41) | 3.51× lower at baseline in the lines without GEM | 0.015 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[KIAA1217]] | B | GEM activity raises KIAA1217's level | lines that do not express GEM (9) vs lines expressing it (41) | 3.78× lower at baseline in the lines without GEM | 0.025 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[CSRNP1]] | B | GEM activity raises CSRNP1's level | lines that do not express GEM (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without GEM | 0.040 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[CXCL8]] | B | GEM activity raises CXCL8's level | lines that do not express GEM (9) vs lines expressing it (41) | 4.16× lower at baseline in the lines without GEM | 0.041 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[BTG1]] | B | GEM activity raises BTG1's level | lines that do not express GEM (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without GEM | 0.042 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[NR3C1]] | B | GEM activity raises NR3C1's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.47× lower at baseline in the lines without GEM | 0.054 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[DLGAP1-AS1]] | B | GEM activity lowers DLGAP1-AS1's level | lines that do not express GEM (9) vs lines expressing it (41) | 1.58× higher at baseline in the lines without GEM | 0.058 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[LIF]] | B | GEM activity raises LIF's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.41× lower at baseline in the lines without GEM | 0.059 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 1.9); signed map (8.8, 28.3). **Vector** length 110, 33.3% of its response variance represented; |z| ≥ 3 in 1,345 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.54 to 5); *KRAS signaling up* (hallmark, mean cos +0.52 to 8); *inflammatory response* (hallmark, mean cos +0.53 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.9 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.8 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +8.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | -0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -4.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.9 | -5.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.9 | -5.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.8 | -3.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.8 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | GTP binding protein overexpressed in skeletal muscle |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:94,249,253-94,262,350 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIR |
| Gene groups (HGNC) | RGK type GTPase family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 2 pathways, smallest: NPAS4 regulates expression of target genes; Transcriptional Regulation by NPAS4 |
| Matched by | ensembl_id |

**Function**, from UniProt [P55040](https://www.uniprot.org/uniprotkb/P55040) (GTP-binding protein GEM):

> Could be a regulatory protein, possibly participating in receptor-mediated signal transduction at the plasma membrane. Has guanine nucleotide-binding activity but undetectable intrinsic GTPase activity.

**Summary**, from NCBI Gene [2669](https://www.ncbi.nlm.nih.gov/gene/2669):

> The protein encoded by this gene belongs to the RAD/GEM family of GTP-binding proteins. It is associated with the inner face of the plasma membrane and could play a role as a regulatory protein in receptor-mediated signal transduction. Alternative splicing occurs at this locus and two transcript variants encoding the same protein have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4234](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4234) · Entrez [2669](https://www.ncbi.nlm.nih.gov/gene/2669) · UniProt [P55040](https://www.uniprot.org/uniprotkb/P55040) · Ensembl [ENSG00000164949](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164949)

## Data

Gene col 9040: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9040); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9040, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9040]; `tensor/DDL_lfc|DDL_z.npy` [9040]; `embed/gene_vectors.npy` [9040]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9040 or target_col == 9040). Every well: [[GEM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GEM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
