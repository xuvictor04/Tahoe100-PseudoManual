---
symbol: "KIF3B"
type: "gene"
col: 2122
ensembl_id: "ENSG00000101350"
name: "kinesin family member 3B"
location: "20q11.21"
module: 12
arm: "+"
pooled_cpm: 91.92
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 16
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# KIF3B

*kinesin family member 3B* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +23.9, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.748× (z -14.2, q 4e-43, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VTA1]] (+0.63, fdr 1e-05), [[DHX16]] (+0.62, fdr 1e-05), [[NDUFA8]] (+0.61, fdr 9e-06); moves opposite to [[PHC2-AS1]] (-0.54, fdr 5e-05), [[CRNDE]] (-0.53, fdr 3e-05), [[SAP30L-AS1]] (-0.52, fdr 9e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +23.9 | 0e+00 | 42/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.68×** | +17.9 | 0e+00 | 45/48 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +15.7 | 0e+00 | 42/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +15.3 | 0e+00 | 42/48 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +12.9 | 9e-36 | 39/48 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.82×** | +10.8 | 4e-25 | 35/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +9.7 | 3e-20 | 33/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.28×** | +8.6 | 5e-16 | 30/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +7.3 | 2e-11 | 26/48 (J82, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.23×** | +7.1 | 7e-11 | 24/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | **1.21×** | +6.7 | 1e-09 | 23/48 (HOP62, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.22×** | +6.4 | 5e-09 | 25/47 (LS 180, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.20× | +6.2 | 2e-08 | 18/48 (A498, J82, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +6.2 | 3e-08 | 17/48 (Hs 766T, HS-578T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +6.1 | 5e-08 | 17/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +5.5 | 1e-06 | 24/49 (J82, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +4.7 | 9e-05 | 5/48 (A549, SNU-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.29×** | +4.6 | 1e-04 | 15/48 (NCI-H2030, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.28×** | +4.5 | 2e-04 | 17/47 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2122.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -14.2 | 4e-43 | 31/49 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.797×** | -7.6 | 1e-11 | 24/50 (HOP62, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.808×** | -7.1 | 2e-10 | 25/47 (NCI-H460, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.809×** | -7.1 | 2e-10 | 23/48 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.886× | -4.2 | 0.003 | 12/47 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.922× | -4.0 | 0.007 | 0/48 | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.893× | -3.8 | 0.012 | 11/49 (CFPAC-1, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.898× | -3.7 | 0.013 | 14/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[olaparib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.915× | -3.1 | 0.13 | 1/48 (SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 115 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -20.8) |
| [[NCI-H460 (line)]] | wt | 91.4 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +11.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.459× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 141 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +31.1) | [[Dinaciclib (drug)]] 5 µM 0.556× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 86.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +17.6) | — |
| [[A549 (line)]] | wt | 77.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +19.1) | — |
| [[A-172 (line)]] | wt | 85.1 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -13.5) |
| [[LOX-IMVI (line)]] | wt | 85.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -8.7) |
| [[Hs 766T (line)]] | wt | 129 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -11.5) |
| [[HS-578T (line)]] | alt | 101 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -13.1) |
| [[J82 (line)]] | alt | 119 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 56.3 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.454× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 68.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +21.6) | — |
| [[NCI-H2347 (line)]] | alt | 71.0 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 77.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.195× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 87.9 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 3.83× (z +12.8) | — |
| [[A-427 (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 102 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.8) | — |
| [[HEC-1-A (line)]] | alt | 50.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.03× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 105 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.506× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +12.9) | — |
| [[NCI-H1792 (line)]] | alt | 99.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 108 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +19.2) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -14.1) |
| [[SNU-423 (line)]] | alt | 85.7 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.08× (z +8.7) | — |
| [[AsPC-1 (line)]] | alt | 53.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 67.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -8.8) |
| [[C32 (line)]] | wt | 56.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -10.9) |
| [[CHP-212 (line)]] | wt | 73.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -12.2) |
| [[COLO 205 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.386× (z -10.0) ⚠ toxic |
| [[H4 (line)]] | wt | 75.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 123 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 92.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.483× (z -9.0) |
| [[SW 900 (line)]] | alt | 94.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 81.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 77.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VTA1]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[DHX16]] | +0.62 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[NDUFA8]] | +0.61 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[RNF40]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[POP4]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CINP]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[NKIRAS2]] | +0.59 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[ZSCAN26]] | +0.59 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[TTC26]] | +0.59 | +0.55 / +0.49 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 690 |
| [[CSTPP1]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[TBC1D19]] | +0.58 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[LLPH]] | +0.57 | +0.66 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2-AS1]] | -0.54 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[CRNDE]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SAP30L-AS1]] | -0.52 | -0.37 / -0.45 | both halves | 9e-05 |  |
| [[SPX]] | -0.51 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[DNAJC9]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[TRIM7]] | -0.49 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[DPY19L2P3]] | -0.49 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[B3GALNT2]] | -0.49 | -0.45 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KIF3B's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.531). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-32.9, -1.9); signed map (-13.5, -27.8). **Vector** length 114, 29.8% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.1 | +10.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.2 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +23.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +9.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +6.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +4.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -9.4 | -7.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.1 | -14.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -9.0 | -7.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.7 | -7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -0.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -3.8 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.7 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,277,651-32,335,011 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0359, FLA8, KLP-11 |
| Gene groups (HGNC) | Kinesins |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 18 pathways, smallest: Intraflagellar transport; Kinesins; Translocation of SLC2A4 (GLUT4) to the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [O15066](https://www.uniprot.org/uniprotkb/O15066) (Kinesin-like protein KIF3B):

> Microtubule-based molecular motor that transport intracellular cargos, such as vesicles, organelles and protein complexes. Uses ATP hydrolysis to generate force to bind and move along the microtubule (By similarity). Plays a role in cilia formation. Involved in photoreceptor integrity and opsin trafficking in rod photoreceptors. Transports vesicles containing N-methyl-D-aspartate (NMDA) receptor subunit GRIN2A into neuronal dendrites (By similarity).

**Summary**, from NCBI Gene [9371](https://www.ncbi.nlm.nih.gov/gene/9371):

> The protein encoded by this gene acts as a heterodimer with kinesin family member 3A to aid in chromosome movement during mitosis and meiosis. The encoded protein is a plus end-directed microtubule motor and can interact with the SMC3 subunit of the cohesin complex. In addition, the encoded protein may be involved in the intracellular movement of membranous organelles. This protein and kinesin family member 3A form the kinesin II subfamily of the kinesin superfamily. [provided by RefSeq, Jul …

**Accessions** — [HGNC:6320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6320) · Entrez [9371](https://www.ncbi.nlm.nih.gov/gene/9371) · UniProt [O15066](https://www.uniprot.org/uniprotkb/O15066) · Ensembl [ENSG00000101350](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101350)

## Data

Gene col 2122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2122); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2122]; `tensor/DDL_lfc|DDL_z.npy` [2122]; `embed/gene_vectors.npy` [2122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2122 or target_col == 2122). Every well: [[KIF3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
