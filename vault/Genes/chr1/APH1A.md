---
symbol: "APH1A"
type: "gene"
col: 3898
ensembl_id: "ENSG00000117362"
name: "aph-1A gamma-secretase subunit"
location: "1q21.2"
module: 2
arm: "+"
pooled_cpm: 20.18
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# APH1A

*aph-1A gamma-secretase subunit* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.90× (z +14.8, q 0e+00, up in 35 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.21× (z +3.8, q 0.016, up in 17 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (HEC-1-A 3.94×, NCI-H1792 5.69×, CFPAC-1 3.13×, A-172 2.88×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 4.01×, NCI-H460 4.17×, CFPAC-1 3.50×, LS 180 4.69×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.534× (z -12.3, q 3e-32, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSNK2B]] (+0.66, fdr 1e-05), [[GET3]] (+0.61, fdr 1e-05), [[INPPL1]] (+0.59, fdr 1e-05); moves opposite to [[EXOC6]] (-0.54, fdr 2e-05), [[RFESD]] (-0.49, fdr 3e-04), [[TLE6]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3898.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (HEC-1-A 3.94×, NCI-H1792 5.69×, CFPAC-1 3.13×, A-172 2.88×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 4.01×, NCI-H460 4.17×, CFPAC-1 3.50×, LS 180 4.69×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +14.8 | 0e+00 | 35/40 (HEC-1-A, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +14.2 | 2e-43 | 29/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +8.9 | 2e-16 | 25/34 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +7.7 | 1e-12 | 32/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.51×** | +5.7 | 1e-06 | 37/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.016 | 17/48 (SW 900, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.021 | 17/47 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.6 | 0.023 | 10/31 (J82, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.44× | +3.1 | 0.11 | 8/47 (LS 180, J82, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.534×** | -12.3 | 3e-32 | 37/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.673×** | -7.8 | 2e-12 | 38/48 (RPMI-7951, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.655×** | -5.9 | 7e-07 | 30/48 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.667×** | -5.6 | 3e-06 | 29/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.702×** | -4.7 | 2e-04 | 26/46 (NCI-H2030, NCI-H1573, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.705×** | -4.7 | 3e-04 | 20/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.727×** | -4.4 | 7e-04 | 21/46 (LOX-IMVI, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.735×** | -4.3 | 0.001 | 20/47 (KATO III, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.746×** | -4.1 | 0.003 | 20/48 (COLO 205, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.751×** | -4.0 | 0.004 | 19/47 (LoVo, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.768×** | -3.7 | 0.012 | 20/47 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.550×** | -3.4 | 0.035 | 8/48 (AsPC-1, hTERT-HPNE, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.800×** | -3.1 | 0.079 | 8/48 (NCI-H460, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 30.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -10.2) |
| [[A-172 (line)]] | wt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 24.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 22.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -8.5) |
| [[KATO III (line)]] | alt | 23.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.6) ⚠ toxic; transcription drop | [[Tucidinostat (drug)]] 0.5 µM 0.285× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 20.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -17.2) |
| [[NCI-H2347 (line)]] | alt | 30.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +8.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 19.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.01× (z +11.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 20.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.210× (z -10.2) |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.1) |
| [[HOP62 (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -10.1) |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.3) |
| [[LoVo (line)]] | wt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -8.6) |
| [[LS 180 (line)]] | wt | 22.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +9.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +11.2) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.4) |
| [[RKO (line)]] | wt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -13.0) |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -8.6) |
| [[SW480 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSNK2B]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[GET3]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[INPPL1]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[UROD]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[BAP1]] | +0.58 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[GUCD1]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ALKBH6]] | +0.57 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[GMPR2]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[MAVS]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[SH2B1]] | +0.55 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[VPS11]] | +0.54 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[TMEM234]] | +0.54 | +0.38 / +0.57 | both halves | 6e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC6]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[RFESD]] | -0.49 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[TLE6]] | -0.48 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[PGBD1]] | -0.47 | -0.39 / -0.45 | both halves | 5e-05 |  |
| [[THEM4]] | -0.47 | -0.38 / -0.56 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.339). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-16.4, -17.0); signed map (-10.1, -21.7). **Vector** length 58.5, 9.91% of its response variance represented; |z| ≥ 3 in 707 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +0.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.6 | -12.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.5 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.2 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.7 |
|  | [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | aph-1A gamma-secretase subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:150,265,399-150,269,580 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APH-1A, CGI-78 |
| Gene groups (HGNC) | Gamma-secretase complex subunits |
| Hallmark sets | NOTCH_SIGNALING |
| Reactome | 33 pathways, smallest: Noncanonical activation of NOTCH3; NOTCH4 Activation and Transmission of Signal to the Nucleus; Regulated proteolysis of p75NTR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BI3](https://www.uniprot.org/uniprotkb/Q96BI3) (Gamma-secretase subunit APH-1A):

> Non-catalytic subunit of the gamma-secretase complex, an endoprotease complex that catalyzes the intramembrane cleavage of integral membrane proteins such as Notch receptors and APP (amyloid-beta precursor protein). Required for normal gamma-secretase assembly. The gamma-secretase complex plays a role in Notch and Wnt signaling cascades and regulation of downstream processes via its role in processing key regulatory proteins, and by regulating cytosolic CTNNB1 levels (Probable).

**Summary**, from NCBI Gene [51107](https://www.ncbi.nlm.nih.gov/gene/51107):

> This gene encodes a component of the gamma secretase complex that cleaves integral membrane proteins such as Notch receptors and beta-amyloid precursor protein. The gamma secretase complex contains this gene product, or the paralogous anterior pharynx defective 1 homolog B (APH1B), along with the presenilin, nicastrin, and presenilin enhancer-2 proteins. The precise function of this seven-transmembrane-domain protein is unknown though it is suspected of facilitating the association of nicastrin …

**Accessions** — [HGNC:29509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29509) · Entrez [51107](https://www.ncbi.nlm.nih.gov/gene/51107) · UniProt [Q96BI3](https://www.uniprot.org/uniprotkb/Q96BI3) · Ensembl [ENSG00000117362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117362)

## Data

Gene col 3898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3898); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3898]; `tensor/DDL_lfc|DDL_z.npy` [3898]; `embed/gene_vectors.npy` [3898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3898 or target_col == 3898). Every well: [[APH1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APH1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
