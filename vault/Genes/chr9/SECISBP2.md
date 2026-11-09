---
symbol: "SECISBP2"
type: "gene"
col: 11943
ensembl_id: "ENSG00000187742"
name: "SECIS binding protein 2"
location: "9q22.2"
module: 83
arm: "+"
pooled_cpm: 67.72
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# SECISBP2

*SECIS binding protein 2* — 9q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.83× (z +33.3, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.717× (z -5.8, q 3e-06, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNT2-AS1]] (+0.75, fdr 1e-05), [[HCG17]] (+0.68, fdr 4e-05), [[TUG1]] (+0.68, fdr 1e-05); moves opposite to [[DPY30]] (-0.68, fdr 1e-05), [[CDC14B]] (-0.66, fdr 3e-05), [[POLR2I]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.83×** | +33.3 | 0e+00 | 48/49 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.39×** | +21.4 | 0e+00 | 46/48 (HT-29, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +18.8 | 0e+00 | 40/48 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +12.3 | 2e-32 | 37/50 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +9.7 | 5e-20 | 34/48 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.8 | 1e-09 | 31/48 (A-172, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.6 | 3e-09 | 33/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 3e-06 | 28/48 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 3e-06 | 30/48 (NCI-H460, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +4.7 | 2e-04 | 24/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.6 | 3e-04 | 21/37 (A498, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.27×** | +4.2 | 0.001 | 26/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.005 | 21/48 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.005 | 24/49 (NCI-H460, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.24×** | +3.7 | 0.007 | 21/48 (LS 180, SW480, …) | two highest doses |  |
| [[Volasertib (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.021 | 16/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +3.2 | 0.038 | 12/49 (HOP62, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11943.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.717×** | -5.8 | 3e-06 | 36/48 (AsPC-1, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -4.1 | 0.012 | 23/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.808×** | -3.7 | 0.033 | 22/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.760×** | -3.4 | 0.085 | 21/48 (HCT15, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.841× | -3.0 | 0.28 | 18/48 (HT-29, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.1 | 10 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.18× (z +23.5) | — |
| [[A-172 (line)]] | wt | 64.9 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +21.2) | — |
| [[C32 (line)]] | wt | 61.5 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +23.8) | — |
| [[hTERT-HPNE (line)]] | wt | 71.4 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +14.1) | — |
| [[HEC-1-A (line)]] | alt | 82.5 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +25.8) | — |
| [[HOP62 (line)]] | alt | 69.8 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +23.5) | — |
| [[HS-578T (line)]] | alt | 52.8 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.57× (z +17.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 75.0 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +25.8) | — |
| [[NCI-H23 (line)]] | alt | 63.7 | 4 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 53.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +27.3) | — |
| [[LoVo (line)]] | wt | 82.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +18.2) | — |
| [[LOX-IMVI (line)]] | wt | 87.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.78× (z +22.8) | — |
| [[SK-MEL-2 (line)]] | alt | 62.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +22.4) | — |
| [[SNU-423 (line)]] | alt | 65.1 | 5 | 0 | [[Auranofin (drug)]] 5 µM 7.87× (z +17.1) | — |
| [[NCI-H2347 (line)]] | alt | 55.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +26.7) | — |
| [[PANC-1 (line)]] | alt | 57.5 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +13.5) | [[Digitoxin (drug)]] 5 µM 0.439× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 86.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +20.2) | — |
| [[SW48 (line)]] | wt | 74.5 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +14.0) | — |
| [[SW480 (line)]] | alt | 88.1 | 2 | 2 | [[Auranofin (drug)]] 5 µM 4.39× (z +20.2) | [[Ixazomib citrate (drug)]] 5 µM 0.481× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 46.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +35.4) | — |
| [[CFPAC-1 (line)]] | alt | 31.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +19.5) | — |
| [[H4 (line)]] | wt | 76.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.70× (z +13.3) | — |
| [[HCT15 (line)]] | alt | 93.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 4.33× (z +10.8) | — |
| [[Hs 766T (line)]] | wt | 60.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.54× (z +19.8) | — |
| [[KATO III (line)]] | alt | 76.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 63.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +16.5) | — |
| [[Panc 03.27 (line)]] | alt | 55.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.64× (z +25.6) | — |
| [[RPMI-7951 (line)]] | alt | 53.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 8.93× (z +16.1) | — |
| [[SW 900 (line)]] | alt | 42.1 | 3 | 0 | [[Auranofin (drug)]] 5 µM 12.6× (z +17.9) | — |
| [[AN3 CA (line)]] | alt | 56.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.54× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 72.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +22.5) | — |
| [[HT-29 (line)]] | alt | 78.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 9.44× (z +23.5) | — |
| [[J82 (line)]] | alt | 68.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +21.6) | — |
| [[NCI-H1792 (line)]] | alt | 46.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.95× (z +21.8) | — |
| [[NCI-H596 (line)]] | alt | 73.4 | 1 (1 ⚠) | 1 | [[Pentoxifylline (drug)]] 0.05 µM 3.15× (z +9.9) ⚠ transcription drop | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.367× (z -9.2) |
| [[SHP-77 (line)]] | alt | 90.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.24× (z +11.4) | — |
| [[SW 1271 (line)]] | alt | 97.9 | 1 | 1 | [[Auranofin (drug)]] 5 µM 8.02× (z +9.2) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0844× (z -11.0) |
| [[SW1417 (line)]] | alt | 92.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +21.3) | — |
| [[A-427 (line)]] | wt | 55.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.71× (z +8.9) | — |
| [[A549 (line)]] | wt | 74.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.8) | — |
| [[HepG2_C3A (line)]] | wt | 70.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.98× (z +19.2) | — |
| [[NCI-H1573 (line)]] | alt | 71.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +10.5) | — |
| [[SNU-1 (line)]] | wt | 65.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +15.0) | — |
| [[C-33 A (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNT2-AS1]] | +0.75 | +0.75 / +0.54 | both halves | 1e-05 |  |
| [[HCG17]] | +0.68 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[TUG1]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MPDU1]] | +0.68 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ERMAP]] | +0.67 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[UBE2D3-AS1]] | +0.66 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[CHMP3]] | +0.65 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[LRP2BP]] | +0.64 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[LINC00880]] | +0.64 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[HCG18]] | +0.63 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[EFCAB8]] | +0.63 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ADAMTSL4-AS2]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY30]] | -0.68 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[CDC14B]] | -0.66 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[POLR2I]] | -0.66 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[NDUFA12]] | -0.64 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[GPATCH11]] | -0.64 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[TMEM185A]] | -0.64 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[WRAP73]] | -0.64 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[BLVRA]] | -0.62 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[C15orf61]] ⚠ | -0.61 | -0.39 / -0.57 | both halves | 6e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TUBG2]] | -0.61 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[TSPAN33]] | -0.61 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SERAC1]] | -0.61 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[BBS5]] | -0.61 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SECISBP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.0, 8.9); signed map (20.8, -2.7). **Vector** length 117, 33.0% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +21.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +33.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +9.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | +1.5 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.0 | +0.5 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -9.0 | -5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -6.9 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.9 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.2 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.0 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -3.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.8 | -3.0 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -2.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SECIS binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.2 — chr9:89,318,500-89,359,663 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SBP2 |
| Reactome | 3 pathways, smallest: Selenocysteine synthesis; Selenoamino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T21](https://www.uniprot.org/uniprotkb/Q96T21) (Selenocysteine insertion sequence-binding protein 2):

> mRNA-binding protein that binds to the SECIS (selenocysteine insertion sequence) element present in the 3'-UTR of mRNAs encoding selenoproteins and facilitates the incorporation of the rare amino acid selenocysteine. Insertion of selenocysteine at UGA codons is mediated by SECISBP2 and EEFSEC: SECISBP2 (1) specifically binds the SECIS sequence once the 80S ribosome encounters an in-frame UGA codon and (2) contacts the RPS27A/eS31 of the 40S ribosome before ribosome stalling. (3) GTP-bound …

**Summary**, from NCBI Gene [79048](https://www.ncbi.nlm.nih.gov/gene/79048):

> The protein encoded by this gene is one of the essential components of the machinery involved in co-translational insertion of selenocysteine (Sec) into selenoproteins. Sec is encoded by the UGA codon, which normally signals translation termination. The recoding of UGA as Sec codon requires a Sec insertion sequence (SECIS) element; present in the 3' untranslated regions of eukaryotic selenoprotein mRNAs. This protein specifically binds to the SECIS element, which is stimulated by a Sec-specific …

**Accessions** — [HGNC:30972](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30972) · Entrez [79048](https://www.ncbi.nlm.nih.gov/gene/79048) · UniProt [Q96T21](https://www.uniprot.org/uniprotkb/Q96T21) · Ensembl [ENSG00000187742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187742)

## Data

Gene col 11943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11943); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11943]; `tensor/DDL_lfc|DDL_z.npy` [11943]; `embed/gene_vectors.npy` [11943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11943 or target_col == 11943). Every well: [[SECISBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SECISBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
