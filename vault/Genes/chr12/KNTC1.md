---
symbol: "KNTC1"
type: "gene"
col: 11538
ensembl_id: "ENSG00000184445"
name: "kinetochore associated 1"
location: "12q24.31"
module: 6
arm: "+"
pooled_cpm: 53.37
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# KNTC1

*kinetochore associated 1* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.98× (z +19.2, q 0e+00, up in 44 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (AsPC-1 8.74×, LoVo 5.13×, SW1417 5.21×, NCI-H1792 6.21×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 3.69×; ⚠ cell-cycle shift, explains ~39% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.528× (z -7.9, q 1e-12, down in 29 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPH]] (+0.86, fdr 7e-06), [[RAD51AP1]] (+0.86, fdr 7e-06), [[VRK1]] (+0.85, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11538.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (AsPC-1 8.74×, LoVo 5.13×, SW1417 5.21×, NCI-H1792 6.21×, …); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW480 3.69×; ⚠ cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.98×** | +19.2 | 0e+00 | 44/47 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.39×** | +10.4 | 5e-23 | 42/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.15×** | +9.1 | 2e-17 | 39/47 (RKO, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +6.8 | 2e-09 | 36/47 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.72×** | +6.7 | 2e-09 | 37/47 (SW480, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~93% of this change | **1.68×** | +6.2 | 6e-08 | 31/41 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.61×** | +5.9 | 3e-07 | 29/47 (NCI-H2347, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +4.3 | 0.001 | 23/47 (A549, LoVo, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +4.1 | 0.002 | 23/47 (A549, SW480, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.11 | 16/47 (SW1417, MIA PaCa-2, …) | all doses, flat |  |
| [[Folic acid (drug)]] 5 µM |  | 1.19× | +3.1 | 0.11 | 11/47 (Hs 766T, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.528×** | -7.9 | 1e-12 | 29/46 (H4, SNU-1, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -5.6 | 6e-06 | 31/45 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.651×** | -5.3 | 2e-05 | 23/47 (H4, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.740×** | -5.3 | 2e-05 | 34/47 (SW480, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -4.9 | 8e-05 | 30/46 (SW480, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.756×** | -4.9 | 8e-05 | 29/47 (SNU-1, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.673×** | -4.9 | 8e-05 | 31/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.759×** | -4.8 | 1e-04 | 25/47 (MIA PaCa-2, SK-MEL-2, …) | two highest doses | composition shift |
| [[palbociclib (drug)]] 5 µM |  | **0.530×** | -4.1 | 0.002 | 31/46 (SW48, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.791×** | -4.1 | 0.002 | 25/47 (KATO III, LoVo, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.683×** | -3.4 | 0.039 | 23/47 (KATO III, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.695×** | -3.2 | 0.063 | 19/47 (Hs 766T, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.779×** | -3.1 | 0.081 | 21/47 (NCI-H23, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.779×** | -3.1 | 0.081 | 20/47 (SK-MEL-2, C-33 A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.87 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 66.7 | 4 (3 ⚠) | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +12.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.415× (z -8.9) |
| [[H4 (line)]] | wt | 46.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0840× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 62.6 | 2 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.0) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -10.7) |
| [[SW1417 (line)]] | alt | 47.3 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.21× (z +17.5) | — |
| [[C32 (line)]] | wt | 29.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +10.9) | — |
| [[HS-578T (line)]] | alt | 28.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 31.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +14.7) | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +16.0) | — |
| [[SW 900 (line)]] | alt | 35.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.37× (z +13.8) | — |
| [[A549 (line)]] | wt | 38.2 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.07× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 56.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +11.7) | — |
| [[HCT15 (line)]] | alt | 81.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 17.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +13.0) | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.112× (z -10.2) |
| [[J82 (line)]] | alt | 110 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.0) ⚠ cell-cycle shift, explains ~39% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.285× (z -11.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 42.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +18.8) | — |
| [[LOX-IMVI (line)]] | wt | 47.6 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +10.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.0) | — |
| [[NCI-H2347 (line)]] | alt | 34.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 42.9 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +10.9) | [[Homoharringtonine (drug)]] 0.05 µM 0.295× (z -8.8) |
| [[RKO (line)]] | wt | 44.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +15.3) | — |
| [[RPMI-7951 (line)]] | alt | 34.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +12.3) | — |
| [[SNU-1 (line)]] | wt | 35.6 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.126× (z -14.5) |
| [[SNU-423 (line)]] | alt | 38.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +15.8) | — |
| [[A-172 (line)]] | wt | 60.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.369× (z -9.9) |
| [[A498 (line)]] | wt | 65.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.395× (z -9.1) |
| [[AN3 CA (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 22.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.74× (z +19.4) | — |
| [[C-33 A (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.324× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.53× (z +14.7) | — |
| [[COLO 205 (line)]] | alt | 49.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.13× (z +13.4) | — |
| [[HOP62 (line)]] | alt | 63.3 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +9.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[Hs 766T (line)]] | wt | 33.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +11.3) | — |
| [[KATO III (line)]] | alt | 52.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LS 180 (line)]] | wt | 42.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 26.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +16.0) | — |
| [[NCI-H2030 (line)]] | alt | 45.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +10.5) | — |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 76.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.7) | — |
| [[SHP-77 (line)]] | alt | 128 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 51.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.2) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SW48 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.113× (z -11.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 92.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPH]] | +0.86 | +0.83 / +0.85 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 587 |
| [[RAD51AP1]] | +0.86 | +0.85 / +0.87 | both halves | 7e-06 | STRING 644 |
| [[VRK1]] | +0.85 | +0.85 / +0.83 | both halves | 7e-06 | pathway: Mitotic Anaphase |
| [[FANCI]] | +0.85 | +0.86 / +0.87 | both halves | 7e-06 | STRING 638 |
| [[RRM1]] | +0.84 | +0.86 / +0.82 | both halves | 7e-06 | STRING 507 |
| [[ATAD5]] | +0.83 | +0.84 / +0.82 | both halves | 7e-06 | STRING 536 |
| [[BRCA1]] | +0.83 | +0.83 / +0.78 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 849 |
| [[MCM8]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 553 |
| [[GINS1]] | +0.82 | +0.84 / +0.79 | both halves | 7e-06 |  |
| [[MELK]] | +0.82 | +0.86 / +0.83 | both halves | 7e-06 | STRING 704 |
| [[FANCD2]] | +0.82 | +0.86 / +0.80 | both halves | 7e-06 | STRING 810 |
| [[POLQ]] | +0.82 | +0.89 / +0.81 | both halves | 7e-06 | STRING 504 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KNTC1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TCF19]] | B | TCF19 activity raises KNTC1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.34× lower at baseline in the lines without TCF19 | 0.015 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises KNTC1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without E2F8 | 0.040 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[MYBL1]] | B | MYBL1 activity raises KNTC1's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without MYBL1 | 0.069 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises KNTC1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.54× lower at baseline in the lines without FAM111B | 0.084 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers KNTC1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers KNTC1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[MCM10]] | C | MCM10 activity raises KNTC1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.19× lower at baseline in the lines without MCM10 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[DIAPH3]], [[MELK]], [[TK1]] | C | DIAPH3, MELK, TK1 activity raises KNTC1's level | lines that do not express DIAPH3, MELK, TK1 (3) vs lines expressing them (47) | 2.70× lower at baseline in the lines without DIAPH3, MELK, TK1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p; co-absent genes |
| [[MYBL2]] | C | MYBL2 activity raises KNTC1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.51× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[ZNF367]] | C | ZNF367 activity raises KNTC1's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without ZNF367 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises KNTC1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.96× lower at baseline in the lines without DSCC1 | 0.077 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.837). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.8, -45.7); signed map (-39.9, -47.5). **Vector** length 147, 49.4% of its response variance represented; |z| ≥ 3 in 1,172 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 65); *DNA strand elongation* (reactome, mean cos +0.67 to 28); *DNA Replication* (reactome, mean cos +0.65 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +8.8 | +9.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +8.7 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +19.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.8 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +3.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.9 | +2.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.9 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.5 | -5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.1 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -7.6 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -7.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.2 | -5.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.8 | -3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.8 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | kinetochore associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,527,246-122,626,396 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0166, ROD |
| Gene groups (HGNC) | RZZ complex |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [P50748](https://www.uniprot.org/uniprotkb/P50748) (Kinetochore-associated protein 1):

> Essential component of the mitotic checkpoint, which prevents cells from prematurely exiting mitosis. Required for the assembly of the dynein-dynactin and MAD1-MAD2 complexes onto kinetochores. Its function related to the spindle assembly machinery is proposed to depend on its association in the mitotic RZZ complex.

**Summary**, from NCBI Gene [9735](https://www.ncbi.nlm.nih.gov/gene/9735):

> This gene encodes a protein that is one of many involved in mechanisms to ensure proper chromosome segregation during cell division. Experimental evidence indicated that the encoded protein functioned in a similar manner to that of the Drosophila rough deal protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17255](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17255) · Entrez [9735](https://www.ncbi.nlm.nih.gov/gene/9735) · UniProt [P50748](https://www.uniprot.org/uniprotkb/P50748) · Ensembl [ENSG00000184445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184445)

## Data

Gene col 11538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11538); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11538]; `tensor/DDL_lfc|DDL_z.npy` [11538]; `embed/gene_vectors.npy` [11538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11538 or target_col == 11538). Every well: [[KNTC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KNTC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
