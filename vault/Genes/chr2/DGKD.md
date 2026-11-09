---
symbol: "DGKD"
type: "gene"
col: 1170
ensembl_id: "ENSG00000077044"
name: "diacylglycerol kinase delta"
location: "2q37.1"
module: 23
arm: "-"
pooled_cpm: 205.76
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# DGKD

*diacylglycerol kinase delta* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.36× (z +7.9, q 1e-12, up in 29 of 47 measured lines) ⚠ unreliable plate only. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 4 lines (SW480 2.10×, NCI-H1573 3.04×, HT-29 2.32×, HepG2/C3A 2.37×; ⚠ cell-cycle shift, explains ~35% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (SW480 2.14×, NCI-H1573 2.79×, HepG2/C3A 2.59×; ⚠ cell-cycle shift, explains ~20% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 1.92×, NCI-H1573 2.56×; ⚠ cell-cycle shift, explains ~31% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (AsPC-1 3.64×, MIA PaCa-2 2.01×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 2.25×); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (NCI-H1573 2.30×).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.555× (z -21.1, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLNB]] (+0.68, fdr 1e-05), [[PAQR5]] (+0.61, fdr 5e-05), [[PSD3]] (+0.61, fdr 3e-05); moves opposite to [[RAB21]] (-0.70, fdr 1e-05), [[C3orf38]] (-0.69, fdr 1e-05), [[N4BP2L1]] (-0.66, fdr 5e-05).
> It sits in the **-** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1170.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 7 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 4 lines (SW480 2.10×, NCI-H1573 3.04×, HT-29 2.32×, HepG2/C3A 2.37×; ⚠ cell-cycle shift, explains ~35% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (SW480 2.14×, NCI-H1573 2.79×, HepG2/C3A 2.59×; ⚠ cell-cycle shift, explains ~20% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (SW480 1.92×, NCI-H1573 2.56×; ⚠ cell-cycle shift, explains ~31% of this change); [[Auranofin (drug)]] 5 µM in 2 lines (AsPC-1 3.64×, MIA PaCa-2 2.01×); [[Dexamethasone (drug)]] 0.05 µM in 1 line (NCI-H1573 2.25×); [[Betamethasone dipropionate (drug)]] 5 µM in 1 line (NCI-H1573 2.30×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +7.9 | 1e-12 | 29/47 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.30×** | +6.7 | 6e-09 | 25/47 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **1.22×** | +5.2 | 4e-05 | 22/47 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.19× | +4.5 | 8e-04 | 21/47 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 1.19× | +4.4 | 0.001 | 20/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.8 | 0.014 | 15/47 (A-172, SW480, …) | rises with dose |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | 1.15× | +3.5 | 0.041 | 8/47 (HCT15, A549, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 1.14× | +3.3 | 0.080 | 18/47 (SW480, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.091 | 15/47 (AsPC-1, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | 1.13× | +3.0 | 0.14 | 16/46 (SW480, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1170.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.555×** | -21.1 | 0e+00 | 44/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.720×** | -11.7 | 2e-29 | 35/47 (LS 180, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -11.6 | 5e-29 | 38/47 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.724×** | -11.5 | 1e-28 | 28/47 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.643×** | -10.7 | 7e-25 | 29/46 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.654×** | -10.7 | 7e-25 | 31/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.654×** | -10.3 | 4e-23 | 29/44 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.664×** | -8.9 | 6e-17 | 32/45 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.915× | -7.7 | 8e-13 | 3/49 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.729×** | -7.7 | 1e-12 | 35/49 (LS 180, H4, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.766×** | -6.7 | 9e-10 | 26/47 (LoVo, J82, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.770×** | -6.6 | 2e-09 | 28/47 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.795×** | -5.8 | 3e-07 | 25/47 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.647×** | -5.7 | 4e-07 | 25/48 (LS 180, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -5.5 | 1e-06 | 22/47 (HOP62, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.802×** | -5.4 | 3e-06 | 26/47 (J82, LoVo, …) | two highest doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.839× | -4.4 | 3e-04 | 20/46 (NCI-H23, PANC-1, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.876× | -4.2 | 8e-04 | 20/47 (SHP-77, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.850× | -4.1 | 0.001 | 19/47 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.857× | -3.9 | 0.003 | 21/48 (PANC-1, NCI-H23, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 102 | 11 (11 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +13.5) ⚠ cell-cycle shift, explains ~20% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -10.7) |
| [[LoVo (line)]] | wt | 266 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -26.0) |
| [[NCI-H460 (line)]] | wt | 817 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -22.3) |
| [[H4 (line)]] | wt | 703 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -15.5) |
| [[LS 180 (line)]] | wt | 243 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -21.0) |
| [[A549 (line)]] | wt | 560 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -18.7) |
| [[HOP62 (line)]] | alt | 150 | 0 | 8 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -16.9) |
| [[PANC-1 (line)]] | alt | 377 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -20.6) |
| [[J82 (line)]] | alt | 154 | 0 | 6 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.509× (z -13.5) |
| [[Hs 766T (line)]] | wt | 198 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -18.1) |
| [[LOX-IMVI (line)]] | wt | 226 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.285× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 64.9 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +12.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Dexamethasone (drug)]] 0.05 µM 2.25× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 181 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -21.8) |
| [[SHP-77 (line)]] | alt | 352 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -13.3) |
| [[HT-29 (line)]] | alt | 78.2 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.32× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 93.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.59× (z +10.6) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 128 | 2 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.11× (z +10.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 2.01× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.387× (z -17.9) |
| [[NCI-H2030 (line)]] | alt | 301 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.3) |
| [[A-172 (line)]] | wt | 128 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -9.9) |
| [[A498 (line)]] | wt | 179 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -19.1) |
| [[AsPC-1 (line)]] | alt | 158 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.64× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 95.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -12.2) |
| [[KATO III (line)]] | alt | 128 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -11.2) |
| [[RKO (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -17.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 332 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -13.0) |
| [[SW48 (line)]] | wt | 133 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -9.8) |
| [[A-427 (line)]] | wt | 80.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.522× (z -11.2) |
| [[BT-474 (line)]] | alt | 234 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -9.7) |
| [[C32 (line)]] | wt | 62.5 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.517× (z -8.7) |
| [[HS-578T (line)]] | alt | 122 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 76.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.456× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 183 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -28.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -9.6) |
| [[SW 900 (line)]] | alt | 201 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -14.9) |
| [[SW1417 (line)]] | alt | 92.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.8) |
| [[AN3 CA (line)]] | alt | 120 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*26 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLNB]] | +0.68 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PAQR5]] | +0.61 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[PSD3]] | +0.61 | +0.58 / +0.43 | both halves | 3e-05 | same gene group |
| [[TMEM241]] | +0.60 | +0.41 / +0.40 | both halves | 5e-05 |  |
| [[ARHGAP8]] | +0.59 | +0.55 / +0.34 | both halves | 1e-04 |  |
| [[GNA12]] | +0.59 | +0.51 / +0.37 | both halves | 9e-05 | pathway: Platelet activation, signaling and aggregation |
| [[KIF21B]] | +0.57 | +0.58 / +0.28 | both halves | 3e-04 |  |
| [[ZFYVE28]] | +0.57 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[FLNB-AS1]] | +0.57 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[LANCL3]] | +0.57 | +0.57 / +0.33 | both halves | 1e-04 |  |
| [[LPCAT4]] | +0.57 | +0.52 / +0.26 | both halves | 3e-04 |  |
| [[ST6GALNAC4]] | +0.57 | +0.47 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*74 of its nearest partners move opposite, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB21]] | -0.70 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[C3orf38]] | -0.69 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[N4BP2L1]] | -0.66 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[MAIP1]] | -0.62 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[HOXB7]] | -0.61 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[TP53]] | -0.61 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[TSGA10]] | -0.61 | -0.62 / -0.21 | both halves | 7e-04 |  |
| [[CLN5]] | -0.61 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[PLEKHF2]] | -0.61 | -0.53 / -0.49 | both halves | 1e-05 | same gene group |
| [[AHI1-DT]] | -0.61 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[CCDC30]] | -0.60 | -0.60 / -0.22 | both halves | 6e-04 |  |
| [[MTUS1-DT]] | -0.60 | -0.62 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DGKD's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (0.8, 16.7); signed map (-4.5, 44.1). **Vector** length 113, 29.3% of its response variance represented; |z| ≥ 3 in 1,512 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +6.4 | +6.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | +6.4 | +5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.4 | +4.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.1 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.8 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.7 | +2.3 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.1 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.2 | -11.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.9 | -6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -21.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.6 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -11.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -4.2 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -3.5 | -1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.5 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | diacylglycerol kinase delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:233,354,494-233,472,104 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0145, DGKdelta |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Sterile alpha motif domain containing; Diacylglycerol kinase family |
| Reactome | 6 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (q) signalling events; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16760](https://www.uniprot.org/uniprotkb/Q16760) (Diacylglycerol kinase delta):

> Diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids. Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes (Probable). By controlling the levels of diacylglycerol, regulates for instance the PKC and EGF receptor signaling pathways and plays a crucial role …

**Summary**, from NCBI Gene [8527](https://www.ncbi.nlm.nih.gov/gene/8527):

> This gene encodes a cytoplasmic enzyme that phosphorylates diacylglycerol to produce phosphatidic acid. Diacylglycerol and phosphatidic acid are two lipids that act as second messengers in signaling cascades. Their cellular concentrations are regulated by the encoded protein, and so it is thought to play an important role in cellular signal transduction. Alternative splicing results in two transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2851) · Entrez [8527](https://www.ncbi.nlm.nih.gov/gene/8527) · UniProt [Q16760](https://www.uniprot.org/uniprotkb/Q16760) · Ensembl [ENSG00000077044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077044)

## Data

Gene col 1170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1170); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1170]; `tensor/DDL_lfc|DDL_z.npy` [1170]; `embed/gene_vectors.npy` [1170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1170 or target_col == 1170). Every well: [[DGKD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DGKD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
