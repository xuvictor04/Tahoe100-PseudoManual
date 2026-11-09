---
symbol: "ENO2"
type: "gene"
col: 3259
ensembl_id: "ENSG00000111674"
name: "enolase 2"
location: "12p13.31"
module: 180
arm: "+"
pooled_cpm: 153.35
n_lines_expressing: 47
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 10
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# ENO2

*enolase 2* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.16× (z +5.1, q 2e-04, up in 5 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.43× (z +3.8, q 0.039, up in 34 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (SHP-77 3.90×, LoVo 3.23×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.42×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.202× (z -23.7, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HILPDA]] (+0.76, fdr 7e-06), [[FAM162A]] (+0.74, fdr 7e-06), [[NDRG1]] (+0.73, fdr 7e-06); moves opposite to [[MCCC2]] (-0.67, fdr 1e-05), [[ZMYND11]] (-0.66, fdr 1e-05), [[PARVA]] (-0.63, fdr 2e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → cells under [[Homoharringtonine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3259.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 2 lines (SHP-77 3.90×, LoVo 3.23×); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.42×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.1 | 2e-04 | 5/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.039 | 34/45 (SHP-77, LoVo, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.36× | +3.2 | 0.21 | 32/46 (LS 180, A549, …) | top dose only | plate-row cell shift |
| [[Fumaric acid (drug)]] 5 µM |  | 1.36× | +3.1 | 0.21 | 31/46 (NCI-H2347, hTERT-HPNE, …) | top dose only | plate-row cell shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.04× | +3.1 | 0.21 | 36/45 (NCI-H1573, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pimitespib (drug)]] 5 µM |  | 1.95× | +3.0 | 0.24 | 30/45 (NCI-H1573, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3259.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.202×** | -23.7 | 0e+00 | 45/45 (H4, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.352×** | -15.4 | 0e+00 | 46/46 (MIA PaCa-2, SW 1271, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.225×** | -15.0 | 0e+00 | 45/45 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.311×** | -11.8 | 9e-30 | 41/44 (LOX-IMVI, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.216×** | -11.3 | 9e-28 | 44/45 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.516×** | -9.8 | 1e-20 | 43/45 (SNU-1, MIA PaCa-2, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.393×** | -9.4 | 4e-19 | 44/45 (H4, SW 900, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.418×** | -8.8 | 1e-16 | 42/47 (H4, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.445×** | -8.5 | 1e-15 | 42/45 (SW 900, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.494×** | -7.4 | 9e-12 | 41/45 (J82, SW 900, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.436×** | -6.5 | 4e-09 | 37/42 (BT-474, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.526×** | -6.5 | 5e-09 | 41/44 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.554×** | -6.2 | 3e-08 | 31/46 (NCI-H23, H4, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.560×** | -6.1 | 6e-08 | 39/45 (NCI-H23, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.574×** | -5.6 | 9e-07 | 31/41 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.303×** | -5.4 | 2e-06 | 40/46 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.316×** | -5.2 | 7e-06 | 39/45 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.643×** | -4.4 | 4e-04 | 35/44 (SW48, C32, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.755×** | -4.1 | 0.001 | 32/45 (SNU-423, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.592×** | -3.9 | 0.003 | 37/45 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.690×** | -3.9 | 0.003 | 36/45 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.437×** | -3.7 | 0.005 | 37/46 (SNU-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.716×** | -3.3 | 0.024 | 27/45 (HOP62, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3259. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 365 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -30.4) |
| [[LOX-IMVI (line)]] | wt | 239 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -24.6) |
| [[SW 900 (line)]] | alt | 390 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0870× (z -30.0) |
| [[H4 (line)]] | wt | 357 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0699× (z -32.0) |
| [[hTERT-HPNE (line)]] | wt | 259 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -14.3) |
| [[C32 (line)]] | wt | 221 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -18.2) |
| [[SNU-423 (line)]] | alt | 234 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -24.2) |
| [[A549 (line)]] | wt | 124 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -23.5) |
| [[BT-474 (line)]] | alt | 90.1 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -20.1) |
| [[CFPAC-1 (line)]] | alt | 157 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -21.9) |
| [[HOP62 (line)]] | alt | 283 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -25.1) |
| [[Hs 766T (line)]] | wt | 135 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -20.2) |
| [[HS-578T (line)]] | alt | 196 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -23.8) |
| [[NCI-H1792 (line)]] | alt | 190 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -18.0) |
| [[PANC-1 (line)]] | alt | 64.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.9) |
| [[NCI-H1573 (line)]] | alt | 119 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 72.8 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 216 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -17.6) |
| [[NCI-H460 (line)]] | wt | 118 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -18.4) |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -21.9) |
| [[RKO (line)]] | wt | 270 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -20.6) |
| [[A-172 (line)]] | wt | 187 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -19.4) |
| [[HCT15 (line)]] | alt | 208 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -18.4) |
| [[HEC-1-A (line)]] | alt | 171 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -20.9) |
| [[J82 (line)]] | alt | 212 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.1) |
| [[LoVo (line)]] | wt | 144 | 1 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.23× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.191× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 234 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -22.4) |
| [[SNU-1 (line)]] | wt | 445 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -26.8) |
| [[HT-29 (line)]] | alt | 99.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -23.6) |
| [[SK-MEL-2 (line)]] | alt | 227 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -18.4) |
| [[SW 1271 (line)]] | alt | 275 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -18.5) |
| [[SW480 (line)]] | alt | 105 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 57.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -14.1) |
| [[CHP-212 (line)]] | wt | 104 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.7) |
| [[COLO 205 (line)]] | alt | 128 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -9.9) |
| [[SW 1088 (line)]] | alt | 204 | 0 | 3 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0537× (z -13.3) |
| [[SW1417 (line)]] | alt | 78.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -15.5) |
| [[C-33 A (line)]] | alt | 50.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.6) |
| [[KATO III (line)]] | alt | 108 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -12.0) |
| [[LS 180 (line)]] | wt | 132 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -15.3) |
| [[SW48 (line)]] | wt | 194 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -15.8) |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.2) |
| [[SHP-77 (line)]] | alt | 52.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.90× (z +9.7) | — |
| [[A-427 (line)]] | wt | 12.5 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 42.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3259), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HILPDA]] | +0.76 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.74 | +0.69 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[NDRG1]] | +0.73 | +0.79 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[PPP2R5B]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[FUT11]] | +0.71 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.71 | +0.72 / +0.59 | both halves | 7e-06 | pathway: Glucose metabolism; STRING 616 |
| [[NCKIPSD]] | +0.69 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ARID3A]] | +0.68 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ALDOC]] | +0.67 | +0.69 / +0.57 | both halves | 9e-06 | pathway: HALLMARK_HYPOXIA; STRING 957 |
| [[SMAP1]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[ABCB9]] | +0.67 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCCC2]] | -0.67 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[ZMYND11]] | -0.66 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[PARVA]] | -0.63 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[UTP20]] | -0.63 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.63 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[ZMPSTE24]] | -0.63 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[FGD5-AS1]] | -0.62 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[OXCT1]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.60 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[DARS2]] | -0.60 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[ACADM]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[POGLUT1]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ENO2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PARVA]] | B | PARVA activity raises ENO2's level | lines that do not express PARVA (6) vs lines expressing it (44) | 2.81× lower at baseline in the lines without PARVA | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969 |
| [[OXCT1]] | B | OXCT1 activity raises ENO2's level | lines that do not express OXCT1 (8) vs lines expressing it (42) | 2.67× lower at baseline in the lines without OXCT1 | 0.062 | ⚠ within organs, on part of the lines |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Homoharringtonine (drug)]] 0.5 µM | C | ENO2 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2: 0.13× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: NMB |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | ENO2 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2: 0.52× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: NMB |
| cells under [[PH-797804 (drug)]] 5 µM | C | ENO2 activity raises the cells' numbers under PH-797804 5 µM (protects the cells) | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2: 0.40× the cells of the other lines | 0.025 | ⚠ few lines (3 vs 47); across organs; also absent: NMB |
| cells under [[Ipatasertib (drug)]] 5 µM | C | ENO2 activity raises the cells' numbers under Ipatasertib 5 µM (protects the cells) | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2: 0.69× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: NMB |
| cells under [[GSK1059615 (drug)]] 5 µM | C | ENO2 activity raises the cells' numbers under GSK1059615 5 µM (protects the cells) | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2: 0.27× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: NMB |
| cells under [[Harringtonine (drug)]] 0.5 µM | C | ENO2 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2: 0.35× the cells of the other lines | 0.052 | ⚠ few lines (3 vs 47); across organs; also absent: NMB |
| cells under [[Homoharringtonine (drug)]] 5 µM | C | ENO2 activity raises the cells' numbers under Homoharringtonine 5 µM (protects the cells) | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2: 0.17× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: NMB |
| [[NCKIPSD]] | C | ENO2 activity strengthens NCKIPSD's drug response | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2 respond 0.36× as strongly (z diff +3.13); strongest at Dinaciclib 0.05 µM: 1.33x vs 0.52x (z diff +7.1) | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: NMB; target measured in part of the lines; the reference differs; artifact flags |
| cells under [[Futibatinib (drug)]] 5 µM | C | ENO2 activity lowers the cells' numbers under Futibatinib 5 µM (makes them more sensitive) | lines that do not express ENO2 (3) vs lines expressing it (45) | the lines without ENO2: 1.49× the cells of the other lines | 0.078 | ⚠ few lines (3 vs 47); across organs; also absent: NMB |
| [[NMB]] | C | ENO2 activity raises NMB's level | lines that do not express ENO2 (3) vs lines expressing it (47) | 3.01× lower at baseline in the lines without ENO2 | 0.087 | ⚠ few lines (3 vs 47); across organs; also absent: NMB; co-absent with the target |

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.4, -14.9); signed map (-35.6, 25.8). **Vector** length 129, 53.2% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.7 | +3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +6.8 | -7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.7 | -8.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +6.6 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.7 | -3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.1 | +2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +4.0 | +2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -7.3 | -6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -7.0 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -11.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.2 | -5.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.5 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -9.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -2.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | enolase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,913,745-6,923,698 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NSE |
| Gene groups (HGNC) | Enolases |
| Hallmark sets | FATTY_ACID_METABOLISM, APOPTOSIS, UV_RESPONSE_UP, GLYCOLYSIS, HYPOXIA, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 4 pathways, smallest: Gluconeogenesis; Glycolysis; Glucose metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P09104](https://www.uniprot.org/uniprotkb/P09104) (Gamma-enolase):

> Enolase that catalyzes the conversion of 2-phosphoglycerate to phosphoenolpyruvate in glycolysis and the reverse reaction in gluconeogenesis (By similarity). Has neurotrophic and neuroprotective properties on a broad spectrum of central nervous system (CNS) neurons. Binds, in a calcium-dependent manner, to cultured neocortical neurons and promotes cell survival (By similarity).

**Summary**, from NCBI Gene [2026](https://www.ncbi.nlm.nih.gov/gene/2026):

> This gene encodes one of the three enolase isoenzymes found in mammals. This isoenzyme, a homodimer, is found in mature neurons and cells of neuronal origin. A switch from alpha enolase to gamma enolase occurs in neural tissue during development in rats and primates. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3353](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3353) · Entrez [2026](https://www.ncbi.nlm.nih.gov/gene/2026) · UniProt [P09104](https://www.uniprot.org/uniprotkb/P09104) · Ensembl [ENSG00000111674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111674)

## Data

Gene col 3259: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3259); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3259, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3259]; `tensor/DDL_lfc|DDL_z.npy` [3259]; `embed/gene_vectors.npy` [3259]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3259 or target_col == 3259). Every well: [[ENO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
