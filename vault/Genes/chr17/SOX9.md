---
symbol: "SOX9"
type: "gene"
col: 4611
ensembl_id: "ENSG00000125398"
name: "SRY-box transcription factor 9"
location: "17q24.3"
module: 112
arm: "+"
pooled_cpm: 125.56
n_lines_expressing: 42
n_dd_up: 3
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 21
direction_downstream: 29
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# SOX9

*SRY-box transcription factor 9* — 17q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.66× (z +5.8, q 4e-06, up in 28 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A498 7.62×, HepG2/C3A 3.04×, HS-578T 3.41×, hTERT-HPNE 3.79×, …; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 5 lines (MIA PaCa-2 4.19×, A498 4.47×, HOP62 4.17×, PANC-1 2.96×, …); [[Harringtonine (drug)]] 5 µM in 3 lines (A498 7.03×, HOP62 5.22×, SNU-423 3.71×; ⚠ cell-cycle shift, explains ~53% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 3.80×); [[TAK-901 (drug)]] 5 µM in 1 line (SW1417 6.06×).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.416× (z -9.5, q 2e-18, down in 31 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.545× (z -6.8, q 2e-09, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP10]] (+0.66, fdr 9e-06), [[GATA6]] (+0.65, fdr 7e-06), [[EHD1]] (+0.64, fdr 7e-06); moves opposite to [[UBE2K]] (-0.50, fdr 3e-05), [[PDS5A]] (-0.49, fdr 8e-05), [[CMKLR2]] (-0.48, fdr 2e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[ATP1B1]] → it (grade B ⚠); 29 go from it, the strongest it → [[EHD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4611.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (A498 7.62×, HepG2/C3A 3.04×, HS-578T 3.41×, hTERT-HPNE 3.79×, …; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 5 lines (MIA PaCa-2 4.19×, A498 4.47×, HOP62 4.17×, PANC-1 2.96×, …); [[Harringtonine (drug)]] 5 µM in 3 lines (A498 7.03×, HOP62 5.22×, SNU-423 3.71×; ⚠ cell-cycle shift, explains ~53% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 3.80×); [[TAK-901 (drug)]] 5 µM in 1 line (SW1417 6.06×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.8 | 4e-06 | 28/40 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.64×** | +5.4 | 2e-05 | 27/40 (A498, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +4.8 | 3e-04 | 30/41 (SW1417, HepG2/C3A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Methotrexate (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.31 | 20/40 (SNU-423, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4611.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.416×** | -9.5 | 2e-18 | 31/37 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.530×** | -7.1 | 3e-10 | 28/40 (A-172, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.545×** | -6.8 | 2e-09 | 32/40 (A-172, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.550×** | -6.7 | 3e-09 | 30/40 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.571×** | -6.3 | 4e-08 | 25/40 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.569×** | -6.0 | 2e-07 | 32/40 (A-172, SW480, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.595×** | -5.8 | 5e-07 | 33/40 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.611×** | -5.5 | 3e-06 | 24/40 (A549, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.616×** | -5.4 | 4e-06 | 30/40 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Budesonide (drug)]] 5 µM |  | **0.622×** | -5.3 | 6e-06 | 27/40 (HOP62, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **0.747×** | -4.6 | 2e-04 | 26/40 (H4, HS-578T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.674×** | -4.4 | 5e-04 | 20/40 (Hs 766T, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.688×** | -4.2 | 0.001 | 22/40 (hTERT-HPNE, A549, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.772×** | -4.1 | 0.002 | 27/41 (A-172, AN3 CA, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.698×** | -4.0 | 0.002 | 22/40 (A549, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.703×** | -3.9 | 0.003 | 23/40 (HOP62, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.704×** | -3.9 | 0.003 | 22/40 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.715×** | -3.7 | 0.006 | 25/40 (SW48, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4611. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 95.2 | 3 (2 ⚠) | 8 | [[Harringtonine (drug)]] 5 µM 5.22× (z +13.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.17× (z +12.0) | [[Budesonide (drug)]] 5 µM 0.284× (z -10.6) |
| [[Hs 766T (line)]] | wt | 83.8 | 0 | 8 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.201× (z -10.6) |
| [[A-172 (line)]] | wt | 278 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.166× (z -16.5) |
| [[HS-578T (line)]] | alt | 94.0 | 2 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +14.5) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.288× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Budesonide (drug)]] 5 µM 0.317× (z -9.7) |
| [[SNU-423 (line)]] | alt | 210 | 1 (1 ⚠) | 6 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.71× (z +11.1) ⚠ cell-cycle shift, explains ~53% of this change | [[Clobetasol propionate (drug)]] 0.05 µM 0.311× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 237 | 2 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +15.4) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.361× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 163 | 2 | 4 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.19× (z +13.4) | [[Ixazomib citrate (drug)]] 5 µM 0.213× (z -14.4) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.401× (z -8.5) |
| [[PANC-1 (line)]] | alt | 218 | 1 | 5 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.96× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.278× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.371× (z -10.8) |
| [[SNU-1 (line)]] | wt | 182 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0947× (z -30.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.265× (z -12.2) |
| [[SW480 (line)]] | alt | 203 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.335× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.393× (z -10.6) |
| [[A498 (line)]] | wt | 126 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.62× (z +23.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.47× (z +12.0) | — |
| [[A549 (line)]] | wt | 119 | 1 | 3 | [[Harringtonine (drug)]] 0.5 µM 5.06× (z +11.3) | [[Clobetasol propionate (drug)]] 5 µM 0.264× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 133 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.357× (z -8.8) |
| [[SW48 (line)]] | wt | 137 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.186× (z -10.5) |
| [[LS 180 (line)]] | wt | 320 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 84.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.276× (z -10.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 60.4 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +13.1) ⚠ cell-cycle shift, would explain all of this change | [[Clobetasol propionate (drug)]] 5 µM 0.281× (z -8.8) |
| [[NCI-H1573 (line)]] | alt | 41.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +8.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 239 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 227 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.06× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0749× (z -14.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 184 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -10.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 215 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0391× (z -15.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.272× (z -8.7) ⚠ cell-cycle shift, explains ~65% of this change |
| [[H4 (line)]] | wt | 70.6 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 5 µM 0.217× (z -9.2) |
| [[HCT15 (line)]] | alt | 117 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.219× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 124 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0849× (z -21.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 181 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -9.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 136 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 31.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 117 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.266× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.305× (z -8.6) |
| [[SW 1088 (line)]] | alt | 137 | 0 | 1 | — | [[Docetaxel (Trihydrate) (drug)]] 5 µM 0.0544× (z -11.0) |
| [[A-427 (line)]] | wt | 8.27 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.80 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.74 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.80 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4611), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP10]] | +0.66 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[GATA6]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 | STRING 591 |
| [[EHD1]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[NR1D1]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SYNJ2]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[NFKBIE]] | +0.61 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[SFR1]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ARL4C]] | +0.60 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[IER3]] | +0.59 | +0.65 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[PTHLH]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 | STRING 636 |
| [[MARCKS]] | +0.59 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[PDGFB]] | +0.59 | +0.52 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2K]] | -0.50 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[PDS5A]] | -0.49 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[CMKLR2]] | -0.48 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[ADPGK]] | -0.48 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[CCNH]] | -0.48 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 19, C 2. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP1B1]] | B | ATP1B1 activity raises SOX9's level | lines that do not express ATP1B1 (8) vs lines expressing it (42) | 3.25× lower at baseline in the lines without ATP1B1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[IER3]] | B | IER3 activity raises SOX9's level | lines that do not express IER3 (5) vs lines expressing it (45) | 4.95× lower at baseline in the lines without IER3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[IL1A]] | B | IL1A activity raises SOX9's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.66× lower at baseline in the lines without IL1A | 0.010 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[AMIGO2]] | B | AMIGO2 activity raises SOX9's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 2.39× lower at baseline in the lines without AMIGO2 | 0.013 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[FAM107B]] | B | FAM107B activity raises SOX9's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.38× lower at baseline in the lines without FAM107B | 0.014 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[IL1B]] | B | IL1B activity raises SOX9's level | lines that do not express IL1B (30) vs lines expressing it (20) | 1.86× lower at baseline in the lines without IL1B | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA |
| [[GATA6]] | B | GATA6 activity raises SOX9's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without GATA6 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[PTHLH]] | B | PTHLH activity raises SOX9's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 2.02× lower at baseline in the lines without PTHLH | 0.023 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1 |
| [[NCEH1]] | B | NCEH1 activity raises SOX9's level | lines that do not express NCEH1 (6) vs lines expressing it (44) | 3.63× lower at baseline in the lines without NCEH1 | 0.028 | ⚠ within organs, on part of the lines; also absent: KCNK6, SMCO2; maybe low, not absent |
| [[CYP2S1]] | B | CYP2S1 activity raises SOX9's level | lines that do not express CYP2S1 (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without CYP2S1 | 0.040 | ⚠ within organs, on part of the lines; also absent: PLA2R1, LAMC2, LY75 |
| [[C15orf48]] | B | C15orf48 activity raises SOX9's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.24× lower at baseline in the lines without C15orf48 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[EPHA4]] | B | EPHA4 activity raises SOX9's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without EPHA4 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10 |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 28, C 1. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EHD1]] | B | SOX9 activity raises EHD1's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.38× lower at baseline in the lines without SOX9 | 0.002 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[KIAA1217]] | B | SOX9 activity raises KIAA1217's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 4.55× lower at baseline in the lines without SOX9 | 0.005 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[SHB]] | B | SOX9 activity raises SHB's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.95× lower at baseline in the lines without SOX9 | 0.005 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[FAM107B]] | B | SOX9 activity raises FAM107B's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 4.82× lower at baseline in the lines without SOX9 | 0.007 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[CXCL8]] | B | SOX9 activity raises CXCL8's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 3.64× lower at baseline in the lines without SOX9 | 0.007 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[PTHLH]] | B | SOX9 activity raises PTHLH's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.63× lower at baseline in the lines without SOX9 | 0.007 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[IL1A]] | B | SOX9 activity raises IL1A's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 3.34× lower at baseline in the lines without SOX9 | 0.008 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[GATA6]] | B | SOX9 activity raises GATA6's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 3.95× lower at baseline in the lines without SOX9 | 0.011 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[IER3]] | B | SOX9 activity raises IER3's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.68× lower at baseline in the lines without SOX9 | 0.019 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[ATP1B1]] | B | SOX9 activity raises ATP1B1's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.87× lower at baseline in the lines without SOX9 | 0.023 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[VDR]] | B | SOX9 activity raises VDR's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 2.18× lower at baseline in the lines without SOX9 | 0.046 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[IL1B]] | B | SOX9 activity raises IL1B's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 3.20× lower at baseline in the lines without SOX9 | 0.048 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.6, 2.7); signed map (45.1, 12.2). **Vector** length 141, 45.4% of its response variance represented; |z| ≥ 3 in 1,348 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Interleukin-10 signaling* (reactome, mean cos +0.52 to 5); *inflammatory response* (hallmark, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +8.6 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.2 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +2.8 | +1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.8 | -7.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -6.4 | -6.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -6.3 | -4.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -6.1 | -5.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -5.6 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | SRY-box transcription factor 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.3 — chr17:72,121,020-72,126,416 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SRA1; previously CMD1, CMPD1 |
| Gene groups (HGNC) | SRY-box transcription factors |
| Hallmark sets | KRAS_SIGNALING_UP, GLYCOLYSIS |
| Reactome | 7 pathways, smallest: Transcriptional regulation of testis differentiation; Deactivation of the beta-catenin transactivating complex; Transcriptional and post-translational regulation of MITF-M expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [P48436](https://www.uniprot.org/uniprotkb/P48436) (Transcription factor SOX-9):

> Transcription factor that plays a key role in chondrocytes differentiation and skeletal development. Specifically binds the 5'-ACAAAG-3' DNA motif present in enhancers and super-enhancers and promotes expression of genes important for chondrogenesis, including cartilage matrix protein-coding genes COL2A1, COL4A2, COL9A1, COL11A2 and ACAN, SOX5 and SOX6. Also binds to some promoter regions (By similarity). Plays a central role in successive steps of chondrocyte differentiation (By similarity). …

**Summary**, from NCBI Gene [6662](https://www.ncbi.nlm.nih.gov/gene/6662):

> The protein encoded by this gene recognizes the sequence CCTTGAG along with other members of the HMG-box class DNA-binding proteins. It acts during chondrocyte differentiation and, with steroidogenic factor 1, regulates transcription of the anti-Muellerian hormone (AMH) gene. Deficiencies lead to the skeletal malformation syndrome campomelic dysplasia, frequently with sex reversal. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11204) · Entrez [6662](https://www.ncbi.nlm.nih.gov/gene/6662) · UniProt [P48436](https://www.uniprot.org/uniprotkb/P48436) · Ensembl [ENSG00000125398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125398)

## Data

Gene col 4611: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4611); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4611, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4611]; `tensor/DDL_lfc|DDL_z.npy` [4611]; `embed/gene_vectors.npy` [4611]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4611 or target_col == 4611). Every well: [[SOX9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOX9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
