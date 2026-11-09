---
symbol: "TRPM4"
type: "gene"
col: 5078
ensembl_id: "ENSG00000130529"
name: "transient receptor potential cation channel subfamily M member 4"
location: "19q13.33"
module: 94
arm: "+"
pooled_cpm: 20.0
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# TRPM4

*transient receptor potential cation channel subfamily M member 4* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 0.05 µM: 2.93× (z +18.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.649× (z -6.9, q 2e-09, down in 23 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.702× (z -6.1, q 3e-07, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP15]] (+0.73, fdr 3e-05), [[SLC44A2]] (+0.68, fdr 1e-05), [[SLC2A4RG]] (+0.67, fdr 7e-06); moves opposite to [[ILF2]] (-0.44, fdr 8e-05), [[XRCC5]] (-0.43, fdr 7e-05), [[CFAP44]] (-0.41, fdr 8e-05).
> It is in [[Module 094]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5078.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM |  | **2.93×** | +18.6 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **2.44×** | +15.4 | 0e+00 | 44/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.82×** | +14.6 | 0e+00 | 39/48 (PANC-1, NCI-H2030, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **2.17×** | +13.4 | 1e-38 | 45/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.80×** | +9.8 | 1e-20 | 33/48 (hTERT-HPNE, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.32×** | +6.8 | 1e-09 | 25/48 (SW1417, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.011 | 15/48 (A-427, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Osimertinib (mesylate) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.011 | 11/48 (A549, C-33 A, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.16× | +3.7 | 0.013 | 13/48 (NCI-H1792, A549, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.019 | 8/45 (BT-474, SW1417, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.040 | 5/48 (Panc 03.27, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5078.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.649×** | -6.9 | 2e-09 | 23/35 (AN3 CA, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -6.1 | 3e-07 | 23/48 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.718×** | -5.7 | 2e-06 | 22/39 (Panc 03.27, Hs 766T, …) | all doses, flat | composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.540×** | -5.6 | 3e-06 | 21/45 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -4.7 | 3e-04 | 20/47 (LS 180, Hs 766T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.777×** | -4.2 | 0.002 | 22/47 (A-427, hTERT-HPNE, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.846× | -4.1 | 0.003 | 17/48 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.655×** | -3.8 | 0.009 | 13/27 (A-427, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.657×** | -3.8 | 0.009 | 15/48 (A549, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.808×** | -3.6 | 0.021 | 13/32 (HEC-1-A, Panc 03.27, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.866× | -3.5 | 0.021 | 21/48 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.822×** | -3.4 | 0.032 | 14/47 (NCI-H1573, C32, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.830×** | -3.2 | 0.055 | 13/47 (RPMI-7951, HT-29, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.712×** | -3.1 | 0.086 | 13/46 (MIA PaCa-2, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.834× | -3.0 | 0.095 | 9/47 (C32, HCT15, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5078. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 22.2 | 3 | 2 | [[Selinexor (drug)]] 5 µM 2.72× (z +9.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -13.5) |
| [[A549 (line)]] | wt | 26.9 | 1 | 3 (1 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.98× (z +8.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 23.0 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -11.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.227× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 9.35 | 3 | 1 (1 ⚠) | [[Selinexor (drug)]] 0.05 µM 4.80× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.262× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[HEC-1-A (line)]] | alt | 51.4 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[LoVo (line)]] | wt | 20.0 | 2 | 1 | [[Selinexor (drug)]] 0.05 µM 2.93× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 18.2 | 3 | 0 | [[Selinexor (drug)]] 0.05 µM 4.69× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 11.6 | 3 | 0 | [[Selinexor (drug)]] 5 µM 3.50× (z +13.9) | — |
| [[A-427 (line)]] | wt | 18.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0874× (z -17.0) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[H4 (line)]] | wt | 21.6 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.68× (z +9.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 28.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0766× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SHP-77 (line)]] | alt | 8.02 | 1 | 1 | [[Selinexor (drug)]] 5 µM 4.35× (z +8.5) | [[Palmatine (chloride) (drug)]] 0.5 µM 0.122× (z -8.5) |
| [[SW480 (line)]] | alt | 11.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.4) | — |
| [[A498 (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[AsPC-1 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[C-33 A (line)]] | alt | 31.8 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.95× (z +9.3) | — |
| [[C32 (line)]] | wt | 20.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0495× (z -8.9) |
| [[Hs 766T (line)]] | wt | 29.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.213× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 23.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 10.8 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.23× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.128× (z -11.1) ⚠ cell-cycle shift, explains ~9% of this change |
| [[RKO (line)]] | wt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +11.3) | — |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -11.1) |
| [[SNU-423 (line)]] | alt | 5.53 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0706× (z -10.3) |
| [[SW1417 (line)]] | alt | 42.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.1) | — |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5078), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP15]] | +0.73 | +0.43 / +0.86 | both halves | 3e-05 |  |
| [[SLC44A2]] | +0.68 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[SLC2A4RG]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[DOCK6]] | +0.64 | +0.48 / +0.74 | both halves | 2e-05 |  |
| [[NGFR]] | +0.64 | +0.30 / +0.75 | both halves | 2e-04 |  |
| [[NUDT16]] | +0.62 | +0.32 / +0.70 | both halves | 2e-04 |  |
| [[ZNF433]] | +0.61 | +0.32 / +0.79 | both halves | 2e-04 |  |
| [[MIR29B2CHG]] | +0.60 | +0.46 / +0.65 | both halves | 2e-05 |  |
| [[SLC22A18]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[HES7]] | +0.56 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[CAPN5]] | +0.55 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[SLC43A2]] | +0.54 | +0.28 / +0.77 | both halves | 3e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILF2]] | -0.44 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[XRCC5]] | -0.43 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[CFAP44]] | -0.41 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[ANKMY1]] | -0.40 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[XNDC1N]] | -0.39 | -0.36 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.3, 24.9); signed map (14.8, -16.1). **Vector** length 107, 25.2% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +13.4 | +14.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +11.0 | +15.4 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +9.6 | +18.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +6.5 | +13.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.5 | +9.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.2 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.8 | -3.5 |
|  | [[NG25 (drug)]] 5 µM |  | -3.6 | -5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.3 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | transient receptor potential cation channel subfamily M member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,157,741-49,211,836 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20041 |
| Gene groups (HGNC) | Transient receptor potential cation channel subfamily M |
| Reactome | 7 pathways, smallest: Sensory perception of sweet, bitter, and umami (glutamate) taste; Sensory perception of taste; TRP channels |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TD43](https://www.uniprot.org/uniprotkb/Q8TD43) (Transient receptor potential cation channel subfamily M member 4):

> Calcium-activated selective cation channel that mediates membrane depolarization. While it is activated by increase in intracellular Ca(2+), it is impermeable to it. Mediates transport of monovalent cations (Na(+) > K(+) > Cs(+) > Li(+)), leading to depolarize the membrane. It thereby plays a central role in cadiomyocytes, neurons from entorhinal cortex, dorsal root and vomeronasal neurons, endocrine pancreas cells, kidney epithelial cells, cochlea hair cells etc. Participates in T-cell …

**Summary**, from NCBI Gene [54795](https://www.ncbi.nlm.nih.gov/gene/54795):

> The protein encoded by this gene is a calcium-activated nonselective ion channel that mediates transport of monovalent cations across membranes, thereby depolarizing the membrane. The activity of the encoded protein increases with increasing intracellular calcium concentration, but this channel does not transport calcium. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:17993](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17993) · Entrez [54795](https://www.ncbi.nlm.nih.gov/gene/54795) · UniProt [Q8TD43](https://www.uniprot.org/uniprotkb/Q8TD43) · Ensembl [ENSG00000130529](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130529)

## Data

Gene col 5078: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5078); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5078, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5078]; `tensor/DDL_lfc|DDL_z.npy` [5078]; `embed/gene_vectors.npy` [5078]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5078 or target_col == 5078). Every well: [[TRPM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRPM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
