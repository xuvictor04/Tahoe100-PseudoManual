---
symbol: "SEMA4B"
type: "gene"
col: 11613
ensembl_id: "ENSG00000185033"
name: "semaphorin 4B"
location: "15q26.1"
module: 154
arm: "+"
pooled_cpm: 227.29
n_lines_expressing: 46
n_dd_up: 2
n_dd_down: 65
n_dd_up_clean: 2
n_dd_down_clean: 52
in_vector_space: true
direction_upstream: 17
direction_downstream: 11
tags: ["gene", "module/154"]
generated_by: "tahoemap"
---

# SEMA4B

*semaphorin 4B* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 1.71× (z +4.3, q 0.010, up in 25 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (NCI-H1573 12.5×, A498 7.85×, Hs 766T 6.56×, LoVo 4.21×, …); [[PH-797804 (drug)]] 5 µM in 1 line (NCI-H1573 10.6×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 2.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 2.55×).
> Pooled over the cell lines (median), lowered significantly by 65 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.108× (z -48.4, q 0e+00, down in 44 of 44 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDPGP1]] (+0.77, fdr 7e-06, ⚠ read-through risk), [[SHB]] (+0.74, fdr 7e-06), [[CIB1]] (+0.70, fdr 7e-06, ⚠ same locus), [[SLCO4A1]] (+0.64, fdr 1e-05), [[PLAUR]] (+0.64, fdr 1e-05); moves opposite to [[FAIM]] (-0.59, fdr 2e-04), [[ZMYND11]] (-0.54, fdr 3e-04), [[NEXN]] (-0.53, fdr 2e-04).
> It is in [[Module 154]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TNFRSF11A]] → it (grade B ⚠); 11 go from it, the strongest it → [[NDRG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11613.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 5 lines (NCI-H1573 12.5×, A498 7.85×, Hs 766T 6.56×, LoVo 4.21×, …); [[PH-797804 (drug)]] 5 µM in 1 line (NCI-H1573 10.6×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1573 2.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1573 2.55×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **1.71×** | +4.3 | 0.010 | 25/44 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.076 | 24/44 (SW1417, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.24× | +3.4 | 0.15 | 19/43 (LOX-IMVI, SW48, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | 1.50× | +3.3 | 0.15 | 21/45 (NCI-H1573, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.23× | +3.1 | 0.23 | 15/45 (HEC-1-A, COLO 205, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 76 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 65 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11613.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.108×** | -48.4 | 0e+00 | 44/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.162×** | -28.0 | 0e+00 | 43/44 (LoVo, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.177×** | -25.6 | 0e+00 | 44/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.404×** | -19.7 | 0e+00 | 43/45 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.322×** | -17.4 | 0e+00 | 44/44 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.340×** | -16.6 | 0e+00 | 43/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.344×** | -15.8 | 0e+00 | 37/40 (LoVo, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.410×** | -13.7 | 5e-41 | 41/45 (SW 1271, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.450×** | -11.8 | 2e-30 | 38/43 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -11.5 | 7e-29 | 37/44 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.478×** | -11.4 | 3e-28 | 42/44 (PANC-1, NCI-H1573, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.597×** | -11.2 | 1e-27 | 42/44 (C32, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.499×** | -10.7 | 5e-25 | 40/44 (HCT15, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.500×** | -10.7 | 7e-25 | 36/44 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.496×** | -10.4 | 1e-23 | 37/43 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.519×** | -9.7 | 1e-20 | 39/44 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -7.8 | 1e-13 | 29/44 (NCI-H23, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.716×** | -7.2 | 1e-11 | 27/44 (HOP62, SW1417, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.624×** | -7.2 | 1e-11 | 35/44 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.629×** | -7.1 | 2e-11 | 39/44 (LoVo, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11613. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 370 | 1 | 30 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.21× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.0686× (z -48.7) |
| [[C32 (line)]] | wt | 236 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0600× (z -38.6) |
| [[HOP62 (line)]] | alt | 288 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0685× (z -35.6) |
| [[NCI-H23 (line)]] | alt | 207 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -36.0) |
| [[NCI-H460 (line)]] | wt | 135 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0966× (z -36.9) |
| [[LOX-IMVI (line)]] | wt | 155 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -33.4) |
| [[NCI-H2347 (line)]] | alt | 244 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0628× (z -42.1) |
| [[PANC-1 (line)]] | alt | 549 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0531× (z -45.5) |
| [[HT-29 (line)]] | alt | 372 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0485× (z -30.6) |
| [[MIA PaCa-2 (line)]] | alt | 197 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0516× (z -48.2) |
| [[NCI-H1573 (line)]] | alt | 750 | 5 (2 ⚠) | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.5× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.0507× (z -46.3) |
| [[Panc 03.27 (line)]] | alt | 223 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -30.7) |
| [[CFPAC-1 (line)]] | alt | 632 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0505× (z -42.5) |
| [[A549 (line)]] | wt | 389 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0434× (z -44.9) |
| [[COLO 205 (line)]] | alt | 344 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0592× (z -35.7) |
| [[HEC-1-A (line)]] | alt | 104 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -28.0) |
| [[BT-474 (line)]] | alt | 180 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.7) |
| [[Hs 766T (line)]] | wt | 328 | 1 | 9 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.56× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.0802× (z -36.6) |
| [[hTERT-HPNE (line)]] | wt | 132 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -26.8) |
| [[NCI-H1792 (line)]] | alt | 300 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0314× (z -51.0) |
| [[NCI-H2030 (line)]] | alt | 186 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0791× (z -35.4) |
| [[H4 (line)]] | wt | 128 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0904× (z -18.3) |
| [[HS-578T (line)]] | alt | 106 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0922× (z -19.0) |
| [[J82 (line)]] | alt | 95.7 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0818× (z -32.7) |
| [[SNU-423 (line)]] | alt | 90.6 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -27.7) |
| [[A498 (line)]] | wt | 176 | 1 | 7 | [[TAK-901 (drug)]] 5 µM 7.85× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -24.6) |
| [[AsPC-1 (line)]] | alt | 379 | 1 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.77× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -29.3) |
| [[KATO III (line)]] | alt | 158 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -28.8) |
| [[LS 180 (line)]] | wt | 190 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -25.2) |
| [[RPMI-7951 (line)]] | alt | 119 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -27.3) |
| [[SW1417 (line)]] | alt | 97.6 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -20.8) |
| [[A-172 (line)]] | wt | 120 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -29.6) |
| [[HCT15 (line)]] | alt | 164 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -23.2) |
| [[SW 1271 (line)]] | alt | 425 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0799× (z -20.8) |
| [[CHP-212 (line)]] | wt | 135 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -17.2) |
| [[SK-MEL-2 (line)]] | alt | 72.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -18.0) |
| [[SW 900 (line)]] | alt | 153 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -23.5) |
| [[RKO (line)]] | wt | 70.1 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -17.9) |
| [[HepG2_C3A (line)]] | wt | 88.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -15.9) |
| [[SW480 (line)]] | alt | 68.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0799× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.245× (z -16.1) |
| [[SHP-77 (line)]] | alt | 165 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -12.0) |
| [[SW48 (line)]] | wt | 86.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -20.6) |
| [[AN3 CA (line)]] | alt | 68.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0908× (z -10.1) |
| [[SW 1088 (line)]] | alt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -8.7) |
| [[A-427 (line)]] | wt | 32.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 40.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 217 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 21.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11613), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDPGP1]] | +0.77 | +0.68 / +0.69 | both halves | 7e-06 | ⚠ **readthrough risk**: GDPGP1 lies 4.1 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[SHB]] | +0.74 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[CIB1]] | +0.70 | +0.75 / +0.58 | both halves | 7e-06 | ⚠ same locus (0.3 kb: neighbours can correlate without regulation) |
| [[SLCO4A1]] | +0.64 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[PLAUR]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[NDRG1]] | +0.64 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[SERPINB1]] | +0.63 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[UBA6]] | +0.63 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[ETHE1]] | +0.61 | +0.57 / +0.35 | both halves | 1e-04 |  |
| [[KRT15]] | +0.61 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[ZNRF1]] | +0.61 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[ANKRD37]] | +0.61 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[EHBP1L1]] | +0.61 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.61 | +0.66 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | -0.59 | -0.63 / -0.29 | both halves | 2e-04 |  |
| [[ZMYND11]] | -0.54 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[NEXN]] | -0.53 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[BRPF3]] | -0.52 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[KANSL1L]] | -0.51 | -0.61 / -0.25 | both halves | 4e-04 |  |
| [[RCBTB2]] | -0.51 | -0.51 / -0.23 | both halves | 5e-04 |  |
| [[RNF115]] | -0.51 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[EFCAB2]] | -0.51 | -0.66 / -0.04 | ⚠ one half (not replicated) | 0.005 |  |
| [[RCN1]] | -0.51 | -0.37 / -0.25 | both halves | 4e-04 |  |
| [[GATC]] | -0.51 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[RNF146]] | -0.50 | -0.62 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[ZNF280D]] | -0.50 | -0.57 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 14, C 3. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNFRSF11A]] | B | TNFRSF11A activity raises SEMA4B's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.30× lower at baseline in the lines without TNFRSF11A | 0.003 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[CDCP1]] | B | CDCP1 activity raises SEMA4B's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without CDCP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[GPRC5A]] | B | GPRC5A activity raises SEMA4B's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.72× lower at baseline in the lines without GPRC5A | 0.005 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[LINC00887]] | B | LINC00887 activity raises SEMA4B's level | lines that do not express LINC00887 (8) vs lines expressing it (42) | 2.46× lower at baseline in the lines without LINC00887 | 0.011 | ⚠ within organs, on part of the lines; also absent: LINC02036, STAMBPL1, CFAP45; maybe low, not absent |
| [[RIPK4]] | B | RIPK4 activity raises SEMA4B's level | lines that do not express RIPK4 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without RIPK4 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC01589, LINC00511, CRYBG1 |
| [[PLEK2]] | B | PLEK2 activity raises SEMA4B's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.15× lower at baseline in the lines without PLEK2 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[IL1RAP]] | B | IL1RAP activity raises SEMA4B's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 2.62× lower at baseline in the lines without IL1RAP | 0.034 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[ST3GAL1]] | B | ST3GAL1 activity raises SEMA4B's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without ST3GAL1 | 0.036 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[KRT15]] | B | KRT15 activity raises SEMA4B's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.05× lower at baseline in the lines without KRT15 | 0.053 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |
| [[MAP2K1]] | B | MAP2K1 activity raises SEMA4B's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 10.6% of all compounds | 0.066 | ⚠ off-target possible; 4 compounds |
| [[CYTH4]] | B | CYTH4 activity raises SEMA4B's level | lines that do not express CYTH4 (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without CYTH4 | 0.073 | ⚠ within organs, on part of the lines; also absent: CSF3, ADTRP, ADAMTS16; maybe low, not absent |
| [[SLCO4A1]] | B | SLCO4A1 activity raises SEMA4B's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 1.67× lower at baseline in the lines without SLCO4A1 | 0.074 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDRG1]] | C | [[CIB1]], SEMA4B, [[SLC2A1]] activity raises NDRG1's level | lines that do not express CIB1, SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 8.44× lower at baseline in the lines without CIB1, SEMA4B, SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[NIBAN2]] | C | SEMA4B activity raises NIBAN2's level | lines that do not express SEMA4B (4) vs lines expressing it (46) | 6.69× lower at baseline in the lines without SEMA4B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ST3GAL1]] | C | SEMA4B activity raises ST3GAL1's level | lines that do not express SEMA4B (4) vs lines expressing it (46) | 6.56× lower at baseline in the lines without SEMA4B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p |
| [[SHB]] | C | SEMA4B, [[SLC2A1]] activity raises SHB's level | lines that do not express SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 4.14× lower at baseline in the lines without SEMA4B, SLC2A1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[LINC00887]] | C | [[CIB1]], SEMA4B activity raises LINC00887's level | lines that do not express CIB1, SEMA4B (4) vs lines expressing them (46) | 3.28× lower at baseline in the lines without CIB1, SEMA4B | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p; co-absent genes |
| [[RIPK4]] | C | SEMA4B, [[SLC2A1]] activity raises RIPK4's level | lines that do not express SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 5.50× lower at baseline in the lines without SEMA4B, SLC2A1 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |
| [[PLEK2]] | C | [[CIB1]], SEMA4B activity raises PLEK2's level | lines that do not express CIB1, SEMA4B (4) vs lines expressing them (46) | 4.98× lower at baseline in the lines without CIB1, SEMA4B | 0.066 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |
| [[SLCO4A1]] | C | SEMA4B, [[SLC2A1]] activity raises SLCO4A1's level | lines that do not express SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 3.12× lower at baseline in the lines without SEMA4B, SLC2A1 | 0.085 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; co-absent genes |
| [[FAIM]] | C | [[CIB1]], SEMA4B, [[SLC2A1]] activity lowers FAIM's level | lines that do not express CIB1, SEMA4B, SLC2A1 (4) vs lines expressing them (46) | 1.66× higher at baseline in the lines without CIB1, SEMA4B, SLC2A1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SHB, NIBAN2, IER3; maybe low, not absent; its own permutation p; co-absent genes |
| [[HPCAL1]] | C | SEMA4B activity raises HPCAL1's level | lines that do not express SEMA4B (4) vs lines expressing it (46) | 3.10× lower at baseline in the lines without SEMA4B | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent |
| cells under [[Furosemide (drug)]] 0.5 µM | C | SEMA4B's natural level lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | SEMA4B's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.73 | 0.268 over the table, 0.038 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 154]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.5, 2.0); signed map (-4.1, 46.9). **Vector** length 115, 46.2% of its response variance represented; |z| ≥ 3 in 2,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +7.0 | -11.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.8 | -16.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.5 | -17.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.3 | +3.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | +6.2 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +4.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +0.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -6.5 | -11.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.5 | -11.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.4 | -11.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.1 | -6.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.0 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.7 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.9 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.7 | -7.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | semaphorin 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:90,160,604-90,229,679 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SemC, KIAA1745, MGC131831; previously SEMAC |
| Gene groups (HGNC) | Semaphorins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPR2](https://www.uniprot.org/uniprotkb/Q9NPR2) (Semaphorin-4B):

> Inhibits axonal extension by providing local signals to specify territories inaccessible for growing axons.

**Summary**, from NCBI Gene [10509](https://www.ncbi.nlm.nih.gov/gene/10509):

> Predicted to enable chemorepellent activity; neuropilin binding activity; and semaphorin receptor binding activity. Predicted to be involved in several processes, including axon guidance; neural crest cell migration; and semaphorin-plexin signaling pathway. Predicted to be located in membrane and synapse. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10730](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10730) · Entrez [10509](https://www.ncbi.nlm.nih.gov/gene/10509) · UniProt [Q9NPR2](https://www.uniprot.org/uniprotkb/Q9NPR2) · Ensembl [ENSG00000185033](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185033)

## Data

Gene col 11613: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11613); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11613, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11613]; `tensor/DDL_lfc|DDL_z.npy` [11613]; `embed/gene_vectors.npy` [11613]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11613 or target_col == 11613). Every well: [[SEMA4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
