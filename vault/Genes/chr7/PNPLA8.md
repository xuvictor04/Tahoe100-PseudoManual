---
symbol: "PNPLA8"
type: "gene"
col: 5667
ensembl_id: "ENSG00000135241"
name: "patatin like domain 8, phospholipase A2"
location: "7q31.1"
module: 1
arm: "-"
pooled_cpm: 155.05
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 15
n_dd_up_clean: 20
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PNPLA8

*patatin like domain 8, phospholipase A2* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.90× (z +9.5, q 9e-19, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.496× (z -10.0, q 1e-20, down in 39 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.706× (z -5.0, q 1e-04, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXD1]] (+0.68, fdr 7e-06), [[IFT20]] (+0.67, fdr 1e-05), [[SELENOK]] (+0.67, fdr 8e-06); moves opposite to [[TGFBRAP1]] (-0.67, fdr 7e-06), [[PFAS]] (-0.67, fdr 7e-06), [[SF3B3]] (-0.64, fdr 1e-05).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GLRX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5667.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.90×** | +9.5 | 9e-19 | 45/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +9.5 | 9e-19 | 46/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +9.0 | 4e-17 | 42/49 (MIA PaCa-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.76×** | +8.4 | 7e-15 | 44/48 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +8.0 | 1e-13 | 43/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +7.4 | 2e-11 | 38/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +7.1 | 8e-11 | 35/48 (LoVo, BT-474, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.61×** | +7.0 | 2e-10 | 45/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +7.0 | 2e-10 | 41/48 (HT-29, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.59×** | +6.5 | 5e-09 | 43/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +6.1 | 5e-08 | 35/48 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +5.8 | 3e-07 | 35/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +5.6 | 8e-07 | 31/48 (A-427, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.3 | 4e-06 | 31/50 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +5.3 | 4e-06 | 29/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.38×** | +4.8 | 6e-05 | 31/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5667.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.496×** | -10.0 | 1e-20 | 39/44 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.505×** | -9.6 | 2e-19 | 44/49 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.659×** | -6.2 | 1e-07 | 37/48 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.706×** | -5.0 | 1e-04 | 34/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.550×** | -4.6 | 4e-04 | 35/48 (AsPC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -4.0 | 0.006 | 0/50 | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.599×** | -4.0 | 0.006 | 34/48 (AsPC-1, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.606×** | -3.9 | 0.008 | 30/48 (AsPC-1, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.620×** | -3.7 | 0.013 | 32/48 (SW1417, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.788×** | -3.5 | 0.023 | 24/49 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.798×** | -3.3 | 0.043 | 26/48 (LOX-IMVI, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.798×** | -3.2 | 0.071 | 26/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.812×** | -3.1 | 0.080 | 25/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.855× | -3.1 | 0.080 | 20/48 (AsPC-1, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Apalutamide (drug)]] 0.5 µM |  | **0.806×** | -3.0 | 0.080 | 24/48 (NCI-H2030, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.814×** | -3.0 | 0.080 | 23/48 (A549, NCI-H1792, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.080 | 23/48 (A549, SNU-423, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.858× | -3.0 | 0.080 | 16/48 (HT-29, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5667. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 158 | 12 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 5.84× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.406× (z -8.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 143 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 130 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -14.5) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 204 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.51× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -11.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 94.9 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.1) | — |
| [[SW480 (line)]] | alt | 87.2 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +13.2) | — |
| [[LoVo (line)]] | wt | 152 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 216 | 3 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.49× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 176 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -14.3) ⚠ unreliable plate only · without an alert: [[Belumosudil (drug)]] 5 µM 0.441× (z -9.9) |
| [[A-427 (line)]] | wt | 78.9 | 4 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 235 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -11.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.165× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 147 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +12.8) | — |
| [[SK-MEL-2 (line)]] | alt | 197 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.11× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.232× (z -12.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 260 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -12.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 384 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.1) | — |
| [[A-172 (line)]] | wt | 126 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -11.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -13.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 228 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.213× (z -11.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 122 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.5) | — |
| [[HCT15 (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -12.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 100 | 2 | 0 | [[Belinostat (drug)]] 5 µM 2.21× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 150 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 198 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.295× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 117 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.40× (z +9.5) | — |
| [[SNU-423 (line)]] | alt | 172 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.403× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 129 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +8.9) | — |
| [[KATO III (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -15.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 107 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 156 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.45× (z +8.7) | — |
| [[PANC-1 (line)]] | alt | 102 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +9.2) | — |
| [[RKO (line)]] | wt | 139 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.96× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 96.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.60× (z +9.8) | — |
| [[SNU-1 (line)]] | wt | 114 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.87× (z +9.1) | — |
| [[SW 1088 (line)]] | alt | 241 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.129× (z -9.0) |
| [[SW 900 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 131 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 118 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 155 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5667), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXD1]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[IFT20]] | +0.67 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[SELENOK]] | +0.67 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[BNIP3L]] | +0.66 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[DNAJB9]] | +0.66 | +0.66 / +0.63 | both halves | 7e-06 | STRING 533; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[MAP1LC3B]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[RIOK3]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[MACO1]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[STX5-DT]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[RNMT]] | +0.63 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[DPM1]] | +0.62 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[CDK2AP2]] | +0.62 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[CCDC186]] | +0.62 | +0.51 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFBRAP1]] | -0.67 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[PFAS]] | -0.67 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[SF3B3]] | -0.64 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.63 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[ZZZ3]] | -0.63 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[EXOSC10]] | -0.62 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[LTV1]] | -0.61 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[UTP20]] | -0.61 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[MRRF]] | -0.60 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[NOL11]] | -0.59 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[COA7]] | -0.59 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[UTP15]] | -0.58 | -0.49 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLRX]] | B | GLRX activity raises PNPLA8's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.39× lower at baseline in the lines without GLRX | 0.022 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[NDRG1]] | B | NDRG1 activity raises PNPLA8's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.48× lower at baseline in the lines without NDRG1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.616). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (7.8, -40.7); signed map (-40.0, 32.6). **Vector** length 122, 48.6% of its response variance represented; |z| ≥ 3 in 1,380 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +8.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.3 | +4.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +7.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.9 | -6.2 |
|  | [[EX229 (drug)]] 5 µM |  | -6.8 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.6 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.3 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.1 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.1 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.5 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | patatin like domain 8, phospholipase A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:108,470,417-108,569,666 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IPLA2G, IPLA2-2, iPLA2gamma |
| Gene groups (HGNC) | Patatin like phospholipase domain containing |
| Hallmark sets | BILE_ACID_METABOLISM |
| Reactome | 5 pathways, smallest: Acyl chain remodelling of PC; Acyl chain remodelling of PE; Glycerophospholipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP80](https://www.uniprot.org/uniprotkb/Q9NP80) (Calcium-independent phospholipase A2-gamma):

> Calcium-independent and membrane-bound phospholipase, that catalyzes the esterolytic cleavage of fatty acids from glycerophospholipids to yield free fatty acids and lysophospholipids, hence regulating membrane physical properties and the release of lipid second messengers and growth factors. Hydrolyzes phosphatidylethanolamine, phosphatidylcholine and probably phosphatidylinositol with a possible preference for the former. Also has a broad substrate specificity in terms of fatty acid moieties, …

**Summary**, from NCBI Gene [50640](https://www.ncbi.nlm.nih.gov/gene/50640):

> This gene encodes a member of the patatin-like phospholipase domain containing protein family. Members of this family are phospholipases which catalyze the cleavage of fatty acids from membrane phospholipids. The product of this gene is a calcium-independent phospholipase. Mutations in this gene have been associated with mitochondrial myopathy with lactic acidosis. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2015]

**Accessions** — [HGNC:28900](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28900) · Entrez [50640](https://www.ncbi.nlm.nih.gov/gene/50640) · UniProt [Q9NP80](https://www.uniprot.org/uniprotkb/Q9NP80) · Ensembl [ENSG00000135241](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135241)

## Data

Gene col 5667: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5667); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5667, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5667]; `tensor/DDL_lfc|DDL_z.npy` [5667]; `embed/gene_vectors.npy` [5667]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5667 or target_col == 5667). Every well: [[PNPLA8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNPLA8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
