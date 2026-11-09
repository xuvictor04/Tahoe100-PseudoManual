---
symbol: "BCL10-AS1"
type: "gene"
col: 13352
ensembl_id: "ENSG00000223653"
name: "BCL10 antisense RNA 1"
location: "1p22.3"
module: 80
arm: "+"
pooled_cpm: 23.9
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 22
n_dd_up_clean: 18
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# BCL10-AS1

*BCL10 antisense RNA 1* — 1p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.58× (z +30.2, q 0e+00, up in 45 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.537× (z -10.4, q 1e-22, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF341-AS1]] (+0.76, fdr 1e-05), [[PPP1R12A-AS2]] (+0.73, fdr 1e-05), [[GSK3B-DT]] (+0.71, fdr 1e-05); moves opposite to [[RSAD1]] (-0.64, fdr 3e-05), [[BRF1]] (-0.63, fdr 4e-05), [[CEP85]] (-0.63, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[WFDC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.58×** | +30.2 | 0e+00 | 45/45 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.97×** | +16.1 | 0e+00 | 34/48 (NCI-H2347, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +16.0 | 0e+00 | 39/44 (HS-578T, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +15.1 | 0e+00 | 42/48 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.85×** | +14.5 | 1e-45 | 31/46 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +13.6 | 2e-40 | 34/45 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.02×** | +11.8 | 3e-30 | 32/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +11.3 | 1e-27 | 25/36 (NCI-H460, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +10.5 | 3e-24 | 23/33 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +9.5 | 9e-20 | 27/48 (A498, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +8.2 | 9e-15 | 15/29 (LoVo, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +6.6 | 1e-09 | 23/47 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +6.4 | 6e-09 | 20/47 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 6e-06 | 20/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 2e-05 | 19/47 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +4.8 | 5e-05 | 16/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.001 | 13/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.021 | 11/44 (AsPC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.537×** | -10.4 | 1e-22 | 35/47 (CFPAC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.566×** | -9.5 | 4e-19 | 32/48 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.642×** | -7.4 | 2e-11 | 25/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.649×** | -7.2 | 7e-11 | 25/48 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.895× | -6.5 | 9e-09 | 8/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.693×** | -6.1 | 8e-08 | 24/47 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.695×** | -6.1 | 9e-08 | 22/43 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.551×** | -5.2 | 1e-05 | 21/48 (AsPC-1, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.750×** | -5.0 | 4e-05 | 16/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.750×** | -4.5 | 5e-04 | 14/43 (J82, SNU-1, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.627×** | -4.1 | 0.002 | 14/40 (RKO, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.795×** | -3.8 | 0.006 | 15/47 (NCI-H1573, AsPC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.802×** | -3.7 | 0.009 | 15/47 (CFPAC-1, NCI-H1573, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.802×** | -3.7 | 0.009 | 13/47 (AsPC-1, NCI-H1573, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **0.796×** | -3.7 | 0.009 | 10/47 (RKO, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.807×** | -3.6 | 0.012 | 15/47 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.808×** | -3.6 | 0.012 | 12/46 (PANC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 77.9 | 4 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.19× (z +18.9) | [[Panobinostat (drug)]] 5 µM 0.188× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 52.4 | 2 | 5 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.71× (z +11.5) | [[Belinostat (drug)]] 5 µM 0.202× (z -9.8) |
| [[HOP62 (line)]] | alt | 19.4 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +14.0) | [[Adagrasib (drug)]] 0.05 µM 0.595× (z -12.3) ⚠ position not correctable |
| [[A498 (line)]] | wt | 17.3 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +16.1) | — |
| [[NCI-H1573 (line)]] | alt | 57.1 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +10.9) | [[Panobinostat (drug)]] 5 µM 0.132× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 14.4 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.12× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 19.3 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.81× (z +15.2) | — |
| [[CFPAC-1 (line)]] | alt | 104 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -15.3) |
| [[LoVo (line)]] | wt | 14.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 15.8 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +16.9) | — |
| [[Panc 03.27 (line)]] | alt | 45.8 | 3 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +14.6) | [[Panobinostat (drug)]] 0.5 µM 0.265× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 11.1 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.14× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0992× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Roxadustat (drug)]] 0.05 µM 0.123× (z -9.5) |
| [[PANC-1 (line)]] | alt | 29.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.2) | — |
| [[A-172 (line)]] | wt | 9.69 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.76× (z +14.0) | — |
| [[HEC-1-A (line)]] | alt | 20.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.57× (z +12.1) | — |
| [[J82 (line)]] | alt | 24.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.9) | — |
| [[LS 180 (line)]] | wt | 12.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 23.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 31.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.44× (z +11.4) | [[Belinostat (drug)]] 5 µM 0.198× (z -10.5) |
| [[SW 900 (line)]] | alt | 21.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +11.3) | — |
| [[SW1417 (line)]] | alt | 11.4 | 2 | 0 | [[Selinexor (drug)]] 5 µM 4.39× (z +11.4) | — |
| [[SW480 (line)]] | alt | 9.95 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +12.4) | — |
| [[A549 (line)]] | wt | 9.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +10.8) | — |
| [[C32 (line)]] | wt | 14.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 16.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.2) | — |
| [[KATO III (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 18.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.569× (z -11.7) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +10.6) | — |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.580× (z -11.9) ⚠ position not correctable |
| [[RKO (line)]] | wt | 32.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.56× (z +9.7) | — |
| [[A-427 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF341-AS1]] | +0.76 | +0.74 / +0.54 | both halves | 1e-05 | same gene group |
| [[PPP1R12A-AS2]] | +0.73 | +0.66 / +0.50 | both halves | 1e-05 | same gene group |
| [[GSK3B-DT]] | +0.71 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | +0.70 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[BHLHE40-AS1]] | +0.70 | +0.60 / +0.55 | both halves | 1e-05 | same gene group |
| [[MMADHC-DT]] | +0.70 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TBCE-1]] | +0.69 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[LPXN]] | +0.69 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.69 | +0.65 / +0.46 | both halves | 2e-05 | same gene group |
| [[LINC01829]] | +0.68 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[LINC02955]] | +0.68 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[LINC02936]] | +0.68 | +0.65 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSAD1]] | -0.64 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[BRF1]] | -0.63 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[CEP85]] | -0.63 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.61 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[CEP57L1]] | -0.60 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.60 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[ELP1]] | -0.60 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[WRAP73]] | -0.60 | -0.40 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WFDC3]] | B | WFDC3 activity raises BCL10-AS1's level | lines that do not express WFDC3 (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without WFDC3 | 0.003 | ⚠ within organs, on part of the lines; also absent: WFDC10B, QPCT, LANCL3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers BCL10-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CYP27C1]] | B | CYP27C1 activity raises BCL10-AS1's level | lines that do not express CYP27C1 (19) vs lines expressing it (31) | 1.51× lower at baseline in the lines without CYP27C1 | 0.030 | ⚠ within organs, on part of the lines; also absent: CACNG6, ENSG00000289526, RAB31 |
| [[ZHX2]] | B | ZHX2 activity raises BCL10-AS1's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.72× lower at baseline in the lines without ZHX2 | 0.055 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[NR3C1]] | B | NR3C1 activity lowers BCL10-AS1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.5% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises BCL10-AS1's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without ZNF341-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[PLAU]] | B | PLAU activity raises BCL10-AS1's level | lines that do not express PLAU (26) vs lines expressing it (24) | 1.78× lower at baseline in the lines without PLAU | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, 11.7); signed map (22.7, -4.8). **Vector** length 126, 34.3% of its response variance represented; |z| ≥ 3 in 1,352 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.3 | +30.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.1 | +16.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +15.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +9.2 | +16.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.4 | +11.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.3 | -0.3 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.9 | -7.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.9 | -10.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.2 | -7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.9 | -5.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.1 | -4.1 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -3.2 | -2.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | BCL10 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p22.3 — chr1:85,276,388-85,448,124 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55868) · Entrez [646626](https://www.ncbi.nlm.nih.gov/gene/646626) · Ensembl [ENSG00000223653](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223653)

## Data

Gene col 13352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13352); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13352]; `tensor/DDL_lfc|DDL_z.npy` [13352]; `embed/gene_vectors.npy` [13352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13352 or target_col == 13352). Every well: [[BCL10-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL10-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
