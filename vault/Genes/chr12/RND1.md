---
symbol: "RND1"
type: "gene"
col: 10274
ensembl_id: "ENSG00000172602"
name: "Rho family GTPase 1"
location: "12q13.12"
module: 14
arm: "+"
pooled_cpm: 10.59
n_lines_expressing: 41
n_dd_up: 36
n_dd_down: 16
n_dd_up_clean: 26
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 20
direction_downstream: 8
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# RND1

*Rho family GTPase 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.55× (z +24.9, q 0e+00, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.531× (z -5.5, q 1e-05, down in 19 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NEURL3]] (+0.66, fdr 7e-06), [[IL23A]] (+0.65, fdr 7e-06), [[C15orf48]] (+0.64, fdr 1e-05); moves opposite to [[TRMT6]] (-0.52, fdr 8e-05), [[FAM120A]] (-0.50, fdr 3e-05), [[COX10]] (-0.48, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[ELF3]] → it (grade B ⚠); 8 go from it, the strongest it → [[HEATR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10274.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.55×** | +24.9 | 0e+00 | 31/32 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **12.5×** | +22.0 | 0e+00 | 37/37 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.49×** | +17.5 | 0e+00 | 36/37 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.45×** | +16.2 | 0e+00 | 36/37 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.44×** | +15.2 | 0e+00 | 29/32 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.63×** | +14.5 | 1e-45 | 33/34 (CFPAC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.89×** | +9.2 | 2e-18 | 25/31 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +8.1 | 4e-14 | 24/37 (HT-29, A498, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.47×** | +7.6 | 3e-12 | 22/29 (SHP-77, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.29×** | +7.2 | 3e-11 | 23/37 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.23×** | +7.0 | 2e-10 | 23/37 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.89×** | +5.3 | 5e-06 | 11/32 (J82, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +5.2 | 9e-06 | 16/27 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +5.2 | 9e-06 | 21/36 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +4.8 | 5e-05 | 12/36 (SW480, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +4.8 | 6e-05 | 21/35 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.73×** | +4.8 | 6e-05 | 15/37 (CFPAC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.57×** | +4.3 | 5e-04 | 9/33 (HepG2/C3A, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, none with an alert; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10274.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.531×** | -5.5 | 1e-05 | 19/34 (Panc 03.27, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.536×** | -5.5 | 1e-05 | 19/35 (NCI-H1573, NCI-H2347, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.582×** | -4.7 | 4e-04 | 18/37 (NCI-H1792, NCI-H2347, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.592×** | -4.6 | 6e-04 | 20/37 (NCI-H2347, NCI-H1573, …) | all doses, flat |  |
| [[Econazole (drug)]] 5 µM |  | **0.636×** | -4.0 | 0.009 | 14/37 (NCI-H1573, hTERT-HPNE, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.659×** | -3.7 | 0.021 | 16/37 (NCI-H2347, A549, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.661×** | -3.6 | 0.021 | 13/37 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.662×** | -3.6 | 0.021 | 17/37 (NCI-H2347, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.680×** | -3.4 | 0.044 | 14/36 (NCI-H2347, NCI-H1573, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.661×** | -3.4 | 0.046 | 12/33 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.688×** | -3.3 | 0.051 | 17/36 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -3.3 | 0.051 | 15/37 (A549, NCI-H2347, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.499×** | -3.2 | 0.065 | 8/34 (SHP-77, SW 900, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.699×** | -3.1 | 0.066 | 14/37 (NCI-H2347, CFPAC-1, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.700×** | -3.1 | 0.066 | 11/37 (HEC-1-A, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10274. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 43.2 | 3 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.0913× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.232× (z -10.1) |
| [[PANC-1 (line)]] | alt | 3.24 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +15.0) | — |
| [[A549 (line)]] | wt | 21.5 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 7.14× (z +9.5) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.161× (z -8.8) |
| [[SW480 (line)]] | alt | 8.61 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 13.8× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 5.24 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 129× (z +20.3) | — |
| [[KATO III (line)]] | alt | 6.83 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +10.4) | — |
| [[LoVo (line)]] | wt | 7.35 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 26.8× (z +14.5) | — |
| [[A498 (line)]] | wt | 5.38 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.76× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 4.80 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 88.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change |
| [[HOP62 (line)]] | alt | 3.08 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.0× (z +13.0) | — |
| [[HS-578T (line)]] | alt | 6.90 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 11.9× (z +11.3) | [[Clobetasol propionate (drug)]] 0.05 µM 0.158× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 58.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +22.5) | — |
| [[HT-29 (line)]] | alt | 17.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +14.9) | — |
| [[J82 (line)]] | alt | 3.24 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 6.58 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +9.3) | — |
| [[NCI-H1792 (line)]] | alt | 8.32 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 13.0× (z +9.7) | [[Dexamethasone (drug)]] 0.5 µM 0.0654× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 20.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +14.0) | [[Clobetasol propionate (drug)]] 0.5 µM 0.117× (z -10.2) |
| [[SNU-423 (line)]] | alt | 8.71 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.19× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.0725× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[SW1417 (line)]] | alt | 21.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0589× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[C32 (line)]] | wt | 2.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.1× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 3.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.7× (z +10.0) | — |
| [[SW 900 (line)]] | alt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +10.1) | — |
| [[A-172 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10274), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NEURL3]] | +0.66 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[IL23A]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[C15orf48]] | +0.64 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[RIPK2]] | +0.63 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[DUSP10]] | +0.59 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[CDKN2B]] | +0.59 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[RAB24]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PIK3IP1]] | +0.57 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[GRHL1]] | +0.57 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[IER3]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ISG20]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CD40]] | +0.56 | +0.47 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT6]] | -0.52 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[FAM120A]] | -0.50 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[COX10]] | -0.48 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[HEATR1]] | -0.48 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 19, C 1. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3]] | B | ELF3 activity raises RND1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.99× lower at baseline in the lines without ELF3 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[VNN1]] | B | VNN1 activity raises RND1's level | lines that do not express VNN1 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without VNN1 | 0.001 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ENSG00000259925, MUC5B |
| [[IRF6]] | B | IRF6 activity raises RND1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without IRF6 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[MPZL3]] | B | MPZL3 activity raises RND1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without MPZL3 | 0.003 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[FRMD4B]] | B | FRMD4B activity raises RND1's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.39× lower at baseline in the lines without FRMD4B | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[CGNL1]] | B | CGNL1 activity raises RND1's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 2.31× lower at baseline in the lines without CGNL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[DUOX2]] | B | DUOX2 activity raises RND1's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 2.18× lower at baseline in the lines without DUOX2 | 0.007 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB |
| [[CX3CL1]] | B | CX3CL1 activity raises RND1's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.96× lower at baseline in the lines without CX3CL1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[MMP13]] | B | MMP13 activity raises RND1's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 1.86× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[OVOL1]] | B | OVOL1 activity raises RND1's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 2.44× lower at baseline in the lines without OVOL1 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[RASGRP3]] | B | RASGRP3 activity raises RND1's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 1.95× lower at baseline in the lines without RASGRP3 | 0.024 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[RNF223]] | B | RNF223 activity raises RND1's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 2.47× lower at baseline in the lines without RNF223 | 0.027 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEATR1]] | B | RND1 activity lowers HEATR1's level | lines that do not express RND1 (9) vs lines expressing it (41) | 1.52× higher at baseline in the lines without RND1 | 0.032 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[ELF3]] | B | RND1 activity raises ELF3's level | lines that do not express RND1 (9) vs lines expressing it (41) | 4.89× lower at baseline in the lines without RND1 | 0.058 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[CBR3-AS1]] | B | RND1 activity raises CBR3-AS1's level | lines that do not express RND1 (9) vs lines expressing it (41) | 1.86× lower at baseline in the lines without RND1 | 0.065 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[MPZL3]] | B | RND1 activity raises MPZL3's level | lines that do not express RND1 (9) vs lines expressing it (41) | 3.28× lower at baseline in the lines without RND1 | 0.068 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[RNF223]] | B | RND1 activity raises RNF223's level | lines that do not express RND1 (9) vs lines expressing it (41) | 2.09× lower at baseline in the lines without RND1 | 0.070 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[BHLHE40]] | B | RND1 activity strengthens BHLHE40's drug response | lines that do not express RND1 (9) vs lines expressing it (40) | the lines without RND1 respond 0.87× as strongly (z diff +1.72); strongest at Panobinostat 5 µM: 0.46x vs 0.29x (z diff +3.1) | 0.085 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MARCKS]] | B | RND1 activity raises MARCKS's level | lines that do not express RND1 (9) vs lines expressing it (41) | 1.58× lower at baseline in the lines without RND1 | 0.088 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |
| [[OVOL1]] | B | RND1 activity raises OVOL1's level | lines that do not express RND1 (9) vs lines expressing it (41) | 2.47× lower at baseline in the lines without RND1 | 0.096 | ⚠ within organs, on part of the lines; also absent: EPS15-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.0, 1.4); signed map (43.1, 11.4). **Vector** length 97.2, 25.0% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +4.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +15.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +24.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | -0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.8 | +3.5 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -4.0 | -4.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.9 | -5.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.6 | -4.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.5 | -3.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -3.5 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | Rho family GTPase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:48,857,145-48,865,870 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Rho6, ARHS, RHOS |
| Gene groups (HGNC) | Rho family GTPases |
| Reactome | 11 pathways, smallest: Sema4D mediated inhibition of cell attachment and migration; SEMA3A-Plexin repulsion signaling by inhibiting Integrin adhesion; Sema4D induced cell migration and growth-cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92730](https://www.uniprot.org/uniprotkb/Q92730) (Rho-related GTP-binding protein Rho6):

> Lacks intrinsic GTPase activity. Has a low affinity for GDP, and constitutively binds GTP. Controls rearrangements of the actin cytoskeleton. Induces the Rac-dependent neuritic process formation in part by disruption of the cortical actin filaments. Causes the formation of many neuritic processes from the cell body with disruption of the cortical actin filaments.

**Summary**, from NCBI Gene [27289](https://www.ncbi.nlm.nih.gov/gene/27289):

> This gene encodes a protein that belongs to the Rho GTPase family. Members of this family regulate the organization of the actin cytoskeleton in response to extracellular growth factors. A similar protein in rat interacts with a microtubule regulator to control axon extension. [provided by RefSeq, Apr 2014]

**Accessions** — [HGNC:18314](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18314) · Entrez [27289](https://www.ncbi.nlm.nih.gov/gene/27289) · UniProt [Q92730](https://www.uniprot.org/uniprotkb/Q92730) · Ensembl [ENSG00000172602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172602)

## Data

Gene col 10274: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10274); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10274, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10274]; `tensor/DDL_lfc|DDL_z.npy` [10274]; `embed/gene_vectors.npy` [10274]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10274 or target_col == 10274). Every well: [[RND1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RND1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
