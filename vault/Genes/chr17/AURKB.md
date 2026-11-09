---
symbol: "AURKB"
type: "gene"
col: 10987
ensembl_id: "ENSG00000178999"
name: "aurora kinase B"
location: "17p13.1"
module: 67
arm: "+"
pooled_cpm: 21.48
n_lines_expressing: 46
n_dd_up: 18
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 9
direction_downstream: 136
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# AURKB

*aurora kinase B* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (16 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.22× (z +9.2, q 2e-17, up in 24 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 1.36× (z +3.4, q 0.028, up in 13 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 7.70×, LoVo 13.2×, SW480 5.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 8.74×, LoVo 12.0×, NCI-H2030 4.77×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 3.73×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.563× (z -9.3, q 5e-18, down in 32 of 44 measured lines) ⚠ cell-cycle shift, explains ~93% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.744× (z -4.8, q 1e-04, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIFC1]] (+0.92, fdr 7e-06), [[NCAPH]] (+0.92, fdr 7e-06), [[KIF22]] (+0.92, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NEURL1B]] → it (grade B ⚠); 136 go from it, the strongest it → [[PTTG1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 16 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10987.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 7.70×, LoVo 13.2×, SW480 5.37×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HEC-1-A 8.74×, LoVo 12.0×, NCI-H2030 4.77×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 3.73×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **2.22×** | +9.2 | 2e-17 | 24/37 (HEC-1-A, LoVo, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **1.93×** | +7.3 | 7e-11 | 16/31 (HEC-1-A, SW480, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.84×** | +7.0 | 5e-10 | 31/42 (KATO III, J82, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.87×** | +6.7 | 4e-09 | 25/35 (HEC-1-A, LoVo, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.59×** | +5.3 | 1e-05 | 24/40 (NCI-H460, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.52×** | +4.8 | 1e-04 | 25/44 (KATO III, HT-29, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.50×** | +4.6 | 3e-04 | 21/43 (KATO III, NCI-H23, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~97% of this change | **1.52×** | +4.6 | 3e-04 | 21/42 (C-33 A, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +4.0 | 0.003 | 16/44 (NCI-H23, NCI-H460, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +4.0 | 0.003 | 18/43 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +3.5 | 0.021 | 14/44 (HT-29, SW1417, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.028 | 13/44 (A-172, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.2 | 0.064 | 15/40 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.33×** | +3.1 | 0.071 | 10/44 (NCI-H2030, PANC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.31×** | +3.1 | 0.073 | 14/43 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.096 | 5/43 (A549, HT-29, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10987.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | **0.563×** | -9.3 | 5e-18 | 32/44 (NCI-H460, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.466×** | -8.8 | 4e-16 | 36/44 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.478×** | -6.0 | 4e-07 | 29/43 (SNU-1, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.451×** | -5.4 | 8e-06 | 25/44 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.636×** | -5.2 | 2e-05 | 30/44 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.653×** | -4.9 | 9e-05 | 22/43 (A-172, KATO III, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.744×** | -4.8 | 1e-04 | 25/44 (HCT15, RKO, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.715×** | -3.9 | 0.008 | 20/43 (HOP62, SHP-77, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.724×** | -3.7 | 0.013 | 15/43 (Hs 766T, RKO, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **0.726×** | -3.7 | 0.013 | 16/42 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.729×** | -3.6 | 0.015 | 21/43 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.722×** | -3.6 | 0.015 | 9/43 (A-172, COLO 205, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.733×** | -3.6 | 0.015 | 18/43 (C32, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.726×** | -3.5 | 0.015 | 16/43 (LoVo, PANC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.682×** | -3.5 | 0.015 | 14/44 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.477×** | -3.2 | 0.050 | 13/41 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.746×** | -3.1 | 0.054 | 12/43 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.763×** | -3.0 | 0.079 | 16/43 (HOP62, A549, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -2.9 | 0.098 | 13/43 (A498, CHP-212, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.811×** | -2.9 | 0.098 | 15/44 (SK-MEL-2, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.99 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10987. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 46.5 | 0 | 6 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.189× (z -17.9) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.313× (z -12.5) |
| [[A-172 (line)]] | wt | 25.3 | 0 | 5 (4 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.188× (z -15.3) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.361× (z -9.3) |
| [[A549 (line)]] | wt | 23.5 | 0 | 4 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.131× (z -12.3) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.266× (z -11.4) |
| [[LoVo (line)]] | wt | 10.7 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 13.2× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | [[Selinexor (drug)]] 0.5 µM 0.147× (z -9.6) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.261× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.183× (z -12.3) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.188× (z -8.5) |
| [[LS 180 (line)]] | wt | 15.1 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.132× (z -11.7) ⚠ cell-cycle shift, explains ~93% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.118× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 15.2 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0988× (z -19.7) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.108× (z -8.9) |
| [[SW480 (line)]] | alt | 34.2 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.37× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | [[Homoharringtonine (drug)]] 5 µM 0.375× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -9.6) |
| [[H4 (line)]] | wt | 17.6 | 0 | 2 (1 ⚠) | — | [[Amsacrine (drug)]] 0.5 µM 0.0528× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 31.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.70× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | — |
| [[NCI-H2030 (line)]] | alt | 30.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 33.0 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.287× (z -10.7) |
| [[HCT15 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.255× (z -8.9) ⚠ cell-cycle shift, explains ~93% of this change |
| [[KATO III (line)]] | alt | 15.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.103× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0257× (z -15.4) ⚠ cell-cycle shift, explains ~89% of this change |
| [[AN3 CA (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10987), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIFC1]] | +0.92 | +0.92 / +0.88 | both halves | 7e-06 | STRING 906 |
| [[NCAPH]] | +0.92 | +0.92 / +0.87 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 909 |
| [[KIF22]] | +0.92 | +0.91 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 666 |
| [[KIF2C]] | +0.91 | +0.92 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 996 |
| [[KIF15]] | +0.91 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 858 |
| [[NCAPG]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 913 |
| [[CIT]] | +0.90 | +0.89 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 487 |
| [[DEPDC1B]] | +0.90 | +0.88 / +0.86 | both halves | 7e-06 | STRING 682 |
| [[RACGAP1]] | +0.90 | +0.88 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 966 |
| [[KIF18B]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 752 |
| [[CDK1]] | +0.89 | +0.88 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 997 |
| [[CDCA3]] | +0.89 | +0.90 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 933 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEURL1B]] | B | NEURL1B activity raises AURKB's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 2.27× lower at baseline in the lines without NEURL1B | 0.068 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[PIMREG]] | C | PIMREG activity raises AURKB's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 3.11× lower at baseline in the lines without PIMREG | 0.005 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[PBK]] | C | PBK activity raises AURKB's level | lines that do not express PBK (4) vs lines expressing it (46) | 3.46× lower at baseline in the lines without PBK | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[NDC80]] | C | NDC80 activity raises AURKB's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 3.00× lower at baseline in the lines without NDC80 | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[PKMYT1]] | C | PKMYT1 activity raises AURKB's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 4.05× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[C21orf58]], [[SKA3]] | C | C21orf58, SKA3 activity raises AURKB's level | lines that do not express C21orf58, SKA3 (3) vs lines expressing them (47) | 3.92× lower at baseline in the lines without C21orf58, SKA3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises AURKB's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.40× lower at baseline in the lines without CDC20 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises AURKB's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without ACBD7 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises AURKB's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.42× lower at baseline in the lines without FAM72D | 0.077 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

*136 arrows, 136 of them with an alert ⚠; grade A 0, B 0, C 136. Shown: the 12 strongest; 124 more arrows (124 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTTG1]] | C | AURKB activity raises PTTG1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without AURKB | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[DIAPH3]] | C | AURKB activity raises DIAPH3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 4.09× lower at baseline in the lines without AURKB | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[SKA2]] | C | AURKB activity raises SKA2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without AURKB | 0.006 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[TOP2A]] | C | AURKB activity raises TOP2A's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.82× lower at baseline in the lines without AURKB | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[CENPF]] | C | AURKB activity raises CENPF's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.61× lower at baseline in the lines without AURKB | 0.008 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PSRC1]] | C | AURKB activity raises PSRC1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without AURKB | 0.009 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[C9orf40]] | C | AURKB activity raises C9orf40's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.04× lower at baseline in the lines without AURKB | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[TK1]] | C | AURKB activity raises TK1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.07× lower at baseline in the lines without AURKB | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PIMREG]] | C | AURKB activity raises PIMREG's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without AURKB | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[BIRC5]] | C | AURKB activity raises BIRC5's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.94× lower at baseline in the lines without AURKB | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[GMNN]] | C | AURKB activity raises GMNN's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.20× lower at baseline in the lines without AURKB | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[SKA3]] | C | AURKB activity raises SKA3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.57× lower at baseline in the lines without AURKB | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.924). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-36.1, -54.0); signed map (-47.5, -42.4). **Vector** length 123, 40.0% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.75 to 4); *Nucleosome assembly* (reactome, mean cos +0.75 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.3 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.3 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | +3.0 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +2.9 | +5.3 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.5 | +1.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | -7.1 | -9.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -6.9 | -8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~63% of this change | -6.2 | -6.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.0 | -4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.4 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | -2.4 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | aurora kinase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:8,204,733-8,210,600 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Aik2, IPL1, AurB, AIM-1, ARK2, STK5, PPP1R48; previously STK12 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Chromosomal passenger complex; Aurora kinase family |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 28 pathways, smallest: Regulation of MECP2 expression and activity; SUMOylation of DNA replication proteins; Transcriptional Regulation by MECP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GD4](https://www.uniprot.org/uniprotkb/Q96GD4) (Aurora kinase B):

> Serine/threonine-protein kinase component of the chromosomal passenger complex (CPC), a complex that acts as a key regulator of mitosis. The CPC complex has essential functions at the centromere in ensuring correct chromosome alignment and segregation and is required for chromatin-induced microtubule stabilization and spindle assembly. Involved in the bipolar attachment of spindle microtubules to kinetochores and is a key regulator for the onset of cytokinesis during mitosis. Required for …

**Summary**, from NCBI Gene [9212](https://www.ncbi.nlm.nih.gov/gene/9212):

> This gene encodes a member of the aurora kinase subfamily of serine/threonine kinases. The genes encoding the other two members of this subfamily are located on chromosomes 19 and 20. These kinases participate in the regulation of alignment and segregation of chromosomes during mitosis and meiosis through association with microtubules. A pseudogene of this gene is located on chromosome 8. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Sep 2015]

**Accessions** — [HGNC:11390](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11390) · Entrez [9212](https://www.ncbi.nlm.nih.gov/gene/9212) · UniProt [Q96GD4](https://www.uniprot.org/uniprotkb/Q96GD4) · Ensembl [ENSG00000178999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178999)

## Data

Gene col 10987: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10987); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10987, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10987]; `tensor/DDL_lfc|DDL_z.npy` [10987]; `embed/gene_vectors.npy` [10987]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10987 or target_col == 10987). Every well: [[AURKB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AURKB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
