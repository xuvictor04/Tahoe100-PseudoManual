---
symbol: "TRPS1"
type: "gene"
col: 2463
ensembl_id: "ENSG00000104447"
name: "transcriptional repressor GATA binding 1"
location: "8q23.3"
module: 121
arm: "+"
pooled_cpm: 140.95
n_lines_expressing: 36
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# TRPS1

*transcriptional repressor GATA binding 1* — 8q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.26× (z +4.7, q 0.001, up in 16 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.336× (z -15.8, q 0e+00, down in 34 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP24]] (+0.62, fdr 1e-05), [[NFIB]] (+0.53, fdr 3e-05), [[SYNE1]] (+0.52, fdr 4e-05); moves opposite to [[CTNNBIP1]] (-0.56, fdr 8e-05), [[DPP9]] (-0.52, fdr 5e-05), [[STARD3]] (-0.52, fdr 5e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARHGAP24]] → it (grade B ⚠); 3 go from it, the strongest it → [[ARHGAP24]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2463.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +4.7 | 0.001 | 16/34 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.25×** | +4.6 | 0.001 | 19/34 (SW1417, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.36×** | +4.5 | 0.001 | 22/35 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +4.4 | 0.001 | 22/34 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.018 | 19/34 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.085 | 16/33 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.085 | 17/34 (AsPC-1, HOP62, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.27×** | +3.2 | 0.085 | 20/36 (AsPC-1, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.13 | 16/34 (AsPC-1, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2463.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.336×** | -15.8 | 0e+00 | 34/34 (Panc 03.27, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.351×** | -15.2 | 0e+00 | 34/34 (Panc 03.27, KATO III, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.433×** | -12.1 | 1e-31 | 33/34 (HT-29, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.462×** | -10.8 | 8e-25 | 25/30 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.491×** | -9.5 | 2e-19 | 27/32 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.414×** | -8.9 | 7e-17 | 27/35 (LOX-IMVI, HT-29, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.682×** | -7.8 | 4e-13 | 25/35 (CHP-212, NCI-H1792, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.645×** | -6.3 | 2e-08 | 26/34 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -6.2 | 4e-08 | 26/33 (RKO, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.671×** | -5.5 | 2e-06 | 22/36 (LOX-IMVI, SW 900, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.495×** | -5.3 | 5e-06 | 18/26 (Panc 03.27, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.698×** | -5.2 | 1e-05 | 27/34 (SHP-77, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.701×** | -5.1 | 1e-05 | 25/34 (LOX-IMVI, BT-474, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.705×** | -4.9 | 5e-05 | 23/34 (C32, LOX-IMVI, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -4.3 | 6e-04 | 20/34 (PANC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.623×** | -3.6 | 0.011 | 23/34 (HOP62, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.783×** | -3.5 | 0.012 | 20/35 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.777×** | -3.5 | 0.012 | 19/34 (RKO, AsPC-1, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.846× | -3.4 | 0.018 | 15/35 (SW 900, RPMI-7951, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.793×** | -3.1 | 0.057 | 18/34 (BT-474, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.812×** | -3.0 | 0.064 | 17/34 (HT-29, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2463. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 409 | 0 | 11 (10 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -17.8) |
| [[HT-29 (line)]] | alt | 573 | 1 (1 ⚠) | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.225× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.274× (z -14.5) |
| [[KATO III (line)]] | alt | 261 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.243× (z -15.6) |
| [[SHP-77 (line)]] | alt | 169 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.421× (z -9.8) |
| [[SW 900 (line)]] | alt | 224 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.318× (z -11.9) |
| [[SW1417 (line)]] | alt | 182 | 1 (1 ⚠) | 7 (6 ⚠) | [[Selinexor (drug)]] 5 µM 1.76× (z +8.7) ⚠ cell-cycle shift, explains ~65% of this change | [[Panobinostat (drug)]] 5 µM 0.330× (z -12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -9.8) |
| [[CHP-212 (line)]] | wt | 380 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -20.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.205× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 269 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -17.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.272× (z -12.8) |
| [[C32 (line)]] | wt | 234 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -14.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[hTERT-HPNE (line)]] | wt | 217 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -11.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.326× (z -9.6) |
| [[LS 180 (line)]] | wt | 318 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.205× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.339× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 111 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -11.1) |
| [[PANC-1 (line)]] | alt | 188 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -16.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.438× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 118 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.186× (z -18.3) |
| [[COLO 205 (line)]] | alt | 52.0 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.257× (z -9.2) |
| [[HS-578T (line)]] | alt | 502 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -12.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.288× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 167 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.229× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 212 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0865× (z -27.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -13.8) |
| [[BT-474 (line)]] | alt | 688 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.270× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.282× (z -9.2) |
| [[H4 (line)]] | wt | 151 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.253× (z -11.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.332× (z -9.1) |
| [[HOP62 (line)]] | alt | 142 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -16.3) |
| [[NCI-H661 (line)]] | alt | 693 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 99.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -13.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.271× (z -12.0) |
| [[A-427 (line)]] | wt | 46.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +14.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AsPC-1 (line)]] | alt | 138 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.45× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 55.5 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.14× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.334× (z -10.2) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 125 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.373× (z -9.8) |
| [[LoVo (line)]] | wt | 39.9 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.91× (z +12.4) | — |
| [[RPMI-7951 (line)]] | alt | 126 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 68.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.217× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~61% of this change |
| [[A-172 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 13.6 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.59 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 33.5 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.8 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2463), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP24]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[NFIB]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[SYNE1]] | +0.52 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[HECW2]] | +0.52 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[CAMK2D]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[ATF7IP]] | +0.51 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[ZFHX4]] | +0.51 | +0.40 / +0.55 | both halves | 5e-05 | same gene group |
| [[RBMS1]] | +0.50 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[PRKG1]] | +0.50 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[MAPK10]] | +0.50 | +0.50 / +0.37 | both halves | 9e-05 |  |
| [[CNKSR3]] | +0.50 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[PTPN13]] | +0.49 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNBIP1]] | -0.56 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[DPP9]] | -0.52 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[STARD3]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[MTMR14]] | -0.51 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[PLEKHM1P1]] | -0.51 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[MYO9B]] | -0.49 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[SPG7]] | -0.49 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[RAPGEF3]] | -0.49 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[SFI1]] | -0.48 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[SENP5]] | -0.48 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[EHBP1L1]] | -0.47 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[ADGRL1-AS1]] | -0.46 | -0.40 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP24]] | B | ARHGAP24 activity raises TRPS1's level | lines that do not express ARHGAP24 (17) vs lines expressing it (33) | 3.59× lower at baseline in the lines without ARHGAP24 | 0.023 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, GPR176 |
| [[MIR181A1HG]] | B | MIR181A1HG activity raises TRPS1's level | lines that do not express MIR181A1HG (7) vs lines expressing it (43) | 4.41× lower at baseline in the lines without MIR181A1HG | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP24]] | B | TRPS1 activity raises ARHGAP24's level | lines that do not express TRPS1 (14) vs lines expressing it (36) | 4.53× lower at baseline in the lines without TRPS1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, FBXO32, PRDM1 |
| [[PPP2R3B]] | B | TRPS1 activity lowers PPP2R3B's level | lines that do not express TRPS1 (14) vs lines expressing it (36) | 1.60× higher at baseline in the lines without TRPS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, FBXO32, PRDM1 |
| cells under [[palbociclib (drug)]] 5 µM | B | TRPS1 activity raises the cells' numbers under palbociclib 5 µM (protects the cells) | lines that do not express TRPS1 (14) vs lines expressing it (34) | the lines without TRPS1: 0.87× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, FBXO32, PRDM1 |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.3, 16.0); signed map (46.5, 17.0). **Vector** length 102, 29.4% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.0 | +2.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +6.6 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.0 | +4.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | +4.8 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.9 | +3.8 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.1 | -15.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.8 | -15.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.0 | -12.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | transcriptional repressor GATA binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.3 — chr8:115,408,496-115,809,673 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LGCR, GC79 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; GATA zinc finger domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHF7](https://www.uniprot.org/uniprotkb/Q9UHF7) (Zinc finger transcription factor Trps1):

> Transcriptional repressor. Binds specifically to GATA sequences and represses expression of GATA-regulated genes at selected sites and stages in vertebrate development. Regulates chondrocyte proliferation and differentiation. Executes multiple functions in proliferating chondrocytes, expanding the region of distal chondrocytes, activating proliferation in columnar cells and supporting the differentiation of columnar into hypertrophic chondrocytes.

**Summary**, from NCBI Gene [7227](https://www.ncbi.nlm.nih.gov/gene/7227):

> This gene encodes a transcription factor that represses GATA-regulated genes and binds to a dynein light chain protein. Binding of the encoded protein to the dynein light chain protein affects binding to GATA consensus sequences and suppresses its transcriptional activity. Defects in this gene are a cause of tricho-rhino-phalangeal syndrome (TRPS) types I-III. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12340](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12340) · Entrez [7227](https://www.ncbi.nlm.nih.gov/gene/7227) · UniProt [Q9UHF7](https://www.uniprot.org/uniprotkb/Q9UHF7) · Ensembl [ENSG00000104447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104447)

## Data

Gene col 2463: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2463); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2463, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2463]; `tensor/DDL_lfc|DDL_z.npy` [2463]; `embed/gene_vectors.npy` [2463]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2463 or target_col == 2463). Every well: [[TRPS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
