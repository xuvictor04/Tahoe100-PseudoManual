---
symbol: "NR4A2"
type: "gene"
col: 7705
ensembl_id: "ENSG00000153234"
name: "nuclear receptor subfamily 4 group A member 2"
location: "2q24.1"
module: 223
arm: "+"
pooled_cpm: 77.63
n_lines_expressing: 43
n_dd_up: 8
n_dd_down: 50
n_dd_up_clean: 4
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/223"]
generated_by: "tahoemap"
---

# NR4A2

*nuclear receptor subfamily 4 group A member 2* — 2q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 2.01× (z +7.1, q 6e-10, up in 27 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.05 µM: 1.59× (z +4.9, q 2e-04, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (12 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.367× (z -10.6, q 2e-23, down in 38 of 41 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.542× (z -6.4, q 3e-08, down in 30 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR4A3]] (+0.77, fdr 7e-06), [[NR4A1]] (+0.66, fdr 7e-06), [[HES1]] (+0.66, fdr 1e-05); moves opposite to [[HOMER2]] (-0.53, fdr 3e-05), [[MAP4]] (-0.50, fdr 4e-05), [[RAP1GDS1]] (-0.50, fdr 4e-05).
> It is in [[Module 223]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SLITRK6]] → it (grade B ⚠); 9 go from it, the strongest it → [[DUSP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.01×** | +7.1 | 6e-10 | 27/40 (NCI-H460, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.86×** | +6.4 | 5e-08 | 26/41 (NCI-H460, RPMI-7951, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.59×** | +4.9 | 2e-04 | 25/41 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.46×** | +4.0 | 0.008 | 21/40 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.017 | 26/42 (NCI-H2347, RPMI-7951, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.6 | 0.028 | 19/41 (NCI-H460, SK-MEL-2, …) | top dose only | composition shift |
| [[Arbutin (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.078 | 22/41 (A498, A-427, …) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.078 | 11/41 (SW1417, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | 1.33× | +3.1 | 0.12 | 15/41 (LS 180, NCI-H460, …) | top dose only |  |
| [[Aliskiren (drug)]] 5 µM |  | 1.22× | +3.0 | 0.12 | 13/42 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.32× | +3.0 | 0.12 | 17/41 (NCI-H460, AN3 CA, …) | rises with dose |  |
| [[4EGI-1 (drug)]] 5 µM |  | 1.78× | +3.0 | 0.12 | 14/41 (A-427, HT-29, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.367×** | -10.6 | 2e-23 | 38/41 (SW48, SHP-77, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.542×** | -6.4 | 3e-08 | 30/41 (NCI-H1573, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.669×** | -6.0 | 5e-07 | 27/42 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.573×** | -5.8 | 7e-07 | 27/41 (NCI-H1573, SHP-77, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.577×** | -5.8 | 9e-07 | 26/40 (SW 900, NCI-H1573, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.585×** | -5.6 | 2e-06 | 30/41 (SW48, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.596×** | -5.4 | 5e-06 | 27/41 (SW48, AsPC-1, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **0.352×** | -5.4 | 5e-06 | 31/40 (RPMI-7951, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.612×** | -5.2 | 2e-05 | 23/41 (NCI-H1573, NCI-H23, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.602×** | -5.1 | 2e-05 | 27/40 (NCI-H23, NCI-H1573, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.615×** | -5.1 | 2e-05 | 25/41 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -4.9 | 5e-05 | 28/41 (SW48, LS 180, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.719×** | -4.8 | 7e-05 | 23/41 (SHP-77, HT-29, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.412×** | -4.6 | 2e-04 | 28/41 (hTERT-HPNE, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.635×** | -4.5 | 3e-04 | 27/41 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.632×** | -4.5 | 3e-04 | 23/41 (SHP-77, C32, …) | all doses, flat | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.430×** | -4.4 | 4e-04 | 27/40 (SW 900, SW1417, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.624×** | -4.3 | 5e-04 | 25/43 (C32, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.752×** | -4.2 | 8e-04 | 26/41 (A-427, SW48, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.671×** | -4.2 | 8e-04 | 21/41 (CHP-212, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.553×** | -4.1 | 0.001 | 20/41 (NCI-H23, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 306 | 2 (2 ⚠) | 16 (10 ⚠) | [[Harringtonine (drug)]] 5 µM 3.82× (z +9.9) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 5 µM 0.122× (z -16.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.126× (z -15.8) |
| [[NCI-H460 (line)]] | wt | 203 | 13 (9 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 16.6× (z +17.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 8.29× (z +13.4) | — |
| [[SW48 (line)]] | wt | 412 | 0 | 12 (9 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0620× (z -17.5) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.120× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 144 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.313× (z -10.8) |
| [[SHP-77 (line)]] | alt | 135 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -16.8) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.275× (z -10.4) |
| [[C32 (line)]] | wt | 32.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +11.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.43× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 104 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0748× (z -12.5) |
| [[RPMI-7951 (line)]] | alt | 111 | 3 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 14.6× (z +15.1) ⚠ cell-cycle shift, explains ~43% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.165× (z -10.5) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -10.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.297× (z -9.2) |
| [[J82 (line)]] | alt | 19.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +12.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 315 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.47× (z +10.2) ⚠ toxic | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -11.9) |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +14.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.150× (z -11.7) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 80.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.8) ⚠ cell-cycle shift, would explain all of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -10.7) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 85.7 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.19× (z +8.8) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.113× (z -16.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 117 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.245× (z -11.2) |
| [[LS 180 (line)]] | wt | 163 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.220× (z -10.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 59.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 105 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.334× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -9.0) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 144 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0844× (z -8.9) |
| [[A-172 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.93 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 77.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 25.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR4A3]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 842 |
| [[NR4A1]] | +0.66 | +0.73 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 782 |
| [[HES1]] | +0.66 | +0.55 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KLRC2]] | +0.62 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[KLRK1]] | +0.62 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[MIR23AHG]] | +0.59 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SMOC1]] | +0.59 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[KLRC4-KLRK1]] | +0.57 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[CXXC4]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[TCF7L2]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[KLRC3]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[REL]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOMER2]] | -0.53 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[MAP4]] | -0.50 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[RAP1GDS1]] | -0.50 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[ATL3]] | -0.47 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[TOM1L1]] | -0.47 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[SVIL-AS1-1]] | -0.46 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[ZDHHC6]] | -0.46 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[PTPN11]] | -0.46 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[RPE]] | -0.44 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[PSMF1]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[GLRX3]] | -0.44 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[ATP2C1]] | -0.44 | -0.27 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLITRK6]] | B | SLITRK6 activity raises NR4A2's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.39× lower at baseline in the lines without SLITRK6 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4 |
| [[DUSP4]] | B | DUSP4 activity raises NR4A2's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.44× lower at baseline in the lines without DUSP4 | 0.021 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[RDH10]] | B | RDH10 activity raises NR4A2's level | lines that do not express RDH10 (9) vs lines expressing it (41) | 1.93× lower at baseline in the lines without RDH10 | 0.034 | ⚠ within organs, on part of the lines; also absent: SEL1L3, EPB41L4B, JDP2; maybe low, not absent |
| [[HOMER2]] | B | HOMER2 activity lowers NR4A2's level | lines that do not express HOMER2 (11) vs lines expressing it (39) | 1.52× higher at baseline in the lines without HOMER2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF529-AS1, ZNF420, ENSG00000282381; maybe low, not absent |
| [[SLITRK6]] | B | SLITRK6 activity strengthens NR4A2's drug response | lines that do not express SLITRK6 (21) vs lines expressing it (21) | the lines without SLITRK6 respond 0.86× as strongly (z diff +1.20); strongest at Panobinostat 5 µM: 0.63x vs 0.39x (z diff +2.9) | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4; target measured in part of the lines; the reference differs; artifact flags |
| [[SERPINE2]] | B | SERPINE2 activity raises NR4A2's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 1.54× lower at baseline in the lines without SERPINE2 | 0.083 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[RHOV]] | B | RHOV activity raises NR4A2's level | lines that do not express RHOV (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without RHOV | 0.083 | ⚠ within organs, on part of the lines; also absent: GOLT1A, SULT2B1, PLEKHG6 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP4]] | B | NR4A2 activity raises DUSP4's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 5.63× lower at baseline in the lines without NR4A2 | 0.010 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FOS]] | B | NR4A2 activity raises FOS's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 2.06× lower at baseline in the lines without NR4A2 | 0.013 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[AHR]] | B | NR4A2 activity raises AHR's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 3.36× lower at baseline in the lines without NR4A2 | 0.021 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[GLRX3]] | B | NR4A2 activity lowers GLRX3's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.22× higher at baseline in the lines without NR4A2 | 0.038 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MIR23AHG]] | B | NR4A2 activity raises MIR23AHG's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.42× lower at baseline in the lines without NR4A2 | 0.049 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NR4A1]] | B | NR4A2 activity raises NR4A1's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 2.23× lower at baseline in the lines without NR4A2 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PER2]] | B | NR4A2 activity raises PER2's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without NR4A2 | 0.064 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[FBXO33]] | B | NR4A2 activity raises FBXO33's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without NR4A2 | 0.068 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HBP1]] | B | NR4A2 activity raises HBP1's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without NR4A2 | 0.0997 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 223]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.735). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.2, -0.3); signed map (6.4, 27.3). **Vector** length 138, 43.6% of its response variance represented; |z| ≥ 3 in 1,356 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +7.5 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.5 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.1 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.0 | +0.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.8 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.8 | +2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | -1.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.0 | -10.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -7.3 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -6.3 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.7 | -5.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -5.7 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -5.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 4 group A member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.1 — chr2:156,324,437-156,342,348 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TINUR, NOT, RNR1, HZF-3; previously NURR1 |
| Gene groups (HGNC) | Nuclear receptor subfamily 4 group A |
| Hallmark sets | KRAS_SIGNALING_DN, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 4 pathways, smallest: SUMOylation of intracellular receptors; Nuclear Receptor transcription pathway; SUMO E3 ligases SUMOylate target proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P43354](https://www.uniprot.org/uniprotkb/P43354) (Nuclear receptor subfamily 4 group A member 2):

> Transcriptional regulator which is important for the differentiation and maintenance of meso-diencephalic dopaminergic (mdDA) neurons during development. It is crucial for expression of a set of genes such as SLC6A3, SLC18A2, TH and DRD2 which are essential for development of mdDA neurons (By similarity).

**Summary**, from NCBI Gene [4929](https://www.ncbi.nlm.nih.gov/gene/4929):

> This gene encodes a member of the steroid-thyroid hormone-retinoid receptor superfamily. The encoded protein may act as a transcription factor. Mutations in this gene have been associated with disorders related to dopaminergic dysfunction, including Parkinson disease, schizophernia, and manic depression. Misregulation of this gene may be associated with rheumatoid arthritis. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. …

**Accessions** — [HGNC:7981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7981) · Entrez [4929](https://www.ncbi.nlm.nih.gov/gene/4929) · UniProt [P43354](https://www.uniprot.org/uniprotkb/P43354) · Ensembl [ENSG00000153234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153234)

## Data

Gene col 7705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7705); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7705]; `tensor/DDL_lfc|DDL_z.npy` [7705]; `embed/gene_vectors.npy` [7705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7705 or target_col == 7705). Every well: [[NR4A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR4A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
