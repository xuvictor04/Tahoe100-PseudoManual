---
symbol: "MIB1"
type: "gene"
col: 2170
ensembl_id: "ENSG00000101752"
name: "MIB E3 ubiquitin protein ligase 1"
location: "18q11.2"
module: 17
arm: "-"
pooled_cpm: 195.76
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MIB1

*MIB E3 ubiquitin protein ligase 1* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +14.7, q 0e+00, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.345× (z -19.3, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOOK3]] (+0.58, fdr 1e-04), [[CLOCK]] (+0.55, fdr 3e-05), [[GAN]] (+0.54, fdr 7e-06); moves opposite to [[METTL17]] (-0.55, fdr 3e-05), [[STRA6LP]] (-0.53, fdr 2e-05), [[EHMT2]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +14.7 | 0e+00 | 38/49 (Hs 766T, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +12.1 | 3e-31 | 41/48 (HEC-1-A, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +10.0 | 4e-21 | 26/48 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +8.0 | 2e-13 | 25/48 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +6.5 | 9e-09 | 24/50 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 1.20× | +6.0 | 2e-07 | 23/47 (H4, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +5.8 | 6e-07 | 19/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +5.2 | 2e-05 | 19/47 (LS 180, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.16× | +5.1 | 3e-05 | 14/48 (NCI-H1573, A498, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.14× | +4.5 | 4e-04 | 18/47 (NCI-H1792, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.28×** | +4.4 | 5e-04 | 24/45 (NCI-H1792, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.13× | +4.3 | 9e-04 | 14/47 (NCI-H2347, NCI-H1792, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.13× | +4.2 | 0.001 | 17/48 (HOP62, NCI-H2347, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 25/48 (KATO III, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 19/49 (A-172, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.07× | +3.3 | 0.032 | 10/48 (HOP62, SW1417, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.050 | 5/49 (SK-MEL-2, Panc 03.27, …) | top dose only |  |
| [[Pyridoxine (drug)]] 5 µM |  | 1.06× | +3.1 | 0.052 | 0/48 | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.06× | +3.0 | 0.071 | 0/49 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2170.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.345×** | -19.3 | 0e+00 | 49/49 (Panc 03.27, NCI-H23, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -12.1 | 5e-31 | 42/48 (LS 180, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | 0.849× | -5.5 | 9e-06 | 20/47 (NCI-H2030, KATO III, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.852× | -5.3 | 2e-05 | 14/47 (BT-474, SW48, …) | all doses, stronger at high dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.865× | -5.0 | 6e-05 | 14/48 (SW 1088, NCI-H460, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.904× | -4.9 | 8e-05 | 6/48 (RKO, AsPC-1, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.824×** | -4.8 | 1e-04 | 23/48 (hTERT-HPNE, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change | 0.880× | -4.5 | 6e-04 | 17/48 (LS 180, NCI-H1573, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.895× | -3.5 | 0.027 | 10/47 (C-33 A, COLO 205, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.905× | -3.5 | 0.031 | 15/48 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~3% of this change | 0.907× | -3.4 | 0.037 | 13/48 (SW 900, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 0.5 µM |  | 0.874× | -3.3 | 0.040 | 11/49 (RKO, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | 0.837× | -3.2 | 0.053 | 17/49 (Hs 766T, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.971× | -3.1 | 0.081 | 0/50 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.884× | -3.1 | 0.086 | 15/47 (PANC-1, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 191 | 1 | 8 (5 ⚠) | [[Auranofin (drug)]] 5 µM 1.86× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -20.5) |
| [[HOP62 (line)]] | alt | 172 | 6 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +23.1) | [[TAK-901 (drug)]] 5 µM 0.357× (z -10.2) |
| [[A-427 (line)]] | wt | 245 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.318× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 203 | 0 | 4 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.232× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 132 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.80× (z +18.0) | [[TAK-901 (drug)]] 5 µM 0.265× (z -12.2) |
| [[J82 (line)]] | alt | 153 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.311× (z -10.7) |
| [[KATO III (line)]] | alt | 158 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.264× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 341 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.587× (z -9.1) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H23 (line)]] | alt | 228 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.155× (z -17.1) |
| [[NCI-H2347 (line)]] | alt | 132 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 240 | 1 | 2 | [[Auranofin (drug)]] 5 µM 1.65× (z +9.9) | [[TAK-901 (drug)]] 5 µM 0.159× (z -19.1) |
| [[PANC-1 (line)]] | alt | 295 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +16.7) | [[TAK-901 (drug)]] 5 µM 0.460× (z -9.8) |
| [[SW 900 (line)]] | alt | 144 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.7) | — |
| [[AsPC-1 (line)]] | alt | 237 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.57× (z +9.8) | [[TAK-901 (drug)]] 5 µM 0.316× (z -9.4) |
| [[BT-474 (line)]] | alt | 246 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.438× (z -11.0) |
| [[C-33 A (line)]] | alt | 350 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.536× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[C32 (line)]] | wt | 123 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 115 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +18.6) | — |
| [[HepG2_C3A (line)]] | wt | 166 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 199 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.280× (z -10.6) |
| [[HT-29 (line)]] | alt | 143 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.59× (z +16.1) | [[TAK-901 (drug)]] 5 µM 0.371× (z -8.7) |
| [[LoVo (line)]] | wt | 172 | 1 | 1 | [[Auranofin (drug)]] 5 µM 1.72× (z +10.3) | [[TAK-901 (drug)]] 5 µM 0.329× (z -11.2) |
| [[LOX-IMVI (line)]] | wt | 221 | 0 | 2 | — | [[TAK-901 (drug)]] 5 µM 0.307× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 297 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.63× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.79× (z +14.2) | — |
| [[RKO (line)]] | wt | 205 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.284× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 155 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 193 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +13.6) | [[TAK-901 (drug)]] 5 µM 0.262× (z -11.7) |
| [[SW1417 (line)]] | alt | 146 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.72× (z +12.0) | — |
| [[A-172 (line)]] | wt | 250 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.346× (z -10.3) |
| [[AN3 CA (line)]] | alt | 290 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -15.5) |
| [[H4 (line)]] | wt | 252 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.239× (z -9.5) |
| [[Hs 766T (line)]] | wt | 148 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 183 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.460× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~7% of this change |
| [[NCI-H460 (line)]] | wt | 189 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.429× (z -9.7) |
| [[SNU-1 (line)]] | wt | 136 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.213× (z -8.5) |
| [[SNU-423 (line)]] | alt | 136 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.4) | — |
| [[SW48 (line)]] | wt | 168 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.418× (z -8.9) |
| [[A498 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 153 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 225 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 251 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOOK3]] | +0.58 | +0.36 / +0.68 | both halves | 1e-04 | same gene group |
| [[CLOCK]] | +0.55 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[GAN]] | +0.54 | +0.59 / +0.58 | both halves | 7e-06 | same gene group |
| [[PAK2]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[FER]] | +0.53 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ATP11C]] | +0.52 | +0.48 / +0.48 | both halves | 2e-05 | same gene group |
| [[ZNF800]] | +0.51 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[DGKH]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[RO60]] | +0.49 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[METTL21A]] | +0.49 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[LARGE1]] | +0.49 | +0.47 / +0.44 | both halves | 3e-05 | same gene group |
| [[CBL]] | +0.48 | +0.38 / +0.68 | both halves | 7e-05 | same gene group |

## Genes that move opposite

*62 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL17]] | -0.55 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[STRA6LP]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[EHMT2]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 | same gene group |
| [[ACACB]] | -0.52 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[IL11RA]] | -0.52 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[NECAP1]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[MRPS31P4]] | -0.50 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[ZBTB17]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[RASSF4]] | -0.49 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[RHOXF1]] | -0.49 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SNRNP70]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[STAG3L4]] ⚠ | -0.49 | -0.53 / -0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MED30]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MIB1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.464). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-3.8, -6.0); signed map (15.7, -7.5). **Vector** length 137, 41.3% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +12.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +5.0 | +5.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.6 | +4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.8 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -11.5 | -19.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -8.6 | -12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.7 | -2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~7% of this change | -6.5 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -6.5 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.5 | -4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.0 | -4.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -4.4 | -5.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -3.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MIB E3 ubiquitin protein ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:21,704,957-21,870,953 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DIP-1, MIB, KIAA1323, ZZANK2, ZZZ6 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers ZZ-type; Ankyrin repeat domain containing; MicroRNA protein coding host genes; Centriolar satellite proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 16 pathways, smallest: Constitutive Signaling by NOTCH1 HD Domain Mutants; Signaling by NOTCH1 HD Domain Mutants in Cancer; NOTCH2 Activation and Transmission of Signal to the Nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YT6](https://www.uniprot.org/uniprotkb/Q86YT6) (E3 ubiquitin-protein ligase MIB1):

> E3 ubiquitin-protein ligase that mediates ubiquitination of Delta receptors, which act as ligands of Notch proteins. Positively regulates the Delta-mediated Notch signaling by ubiquitinating the intracellular domain of Delta, leading to endocytosis of Delta receptors. Probably mediates ubiquitination and subsequent proteasomal degradation of DAPK1, thereby antagonizing anti-apoptotic effects of DAPK1 to promote TNF-induced apoptosis (By similarity). Involved in ubiquitination of centriolar …

**Summary**, from NCBI Gene [57534](https://www.ncbi.nlm.nih.gov/gene/57534):

> This gene encodes a protein containing multiple ankyrin repeats and RING finger domains that functions as an E3 ubiquitin ligase. The encoded protein positively regulates Notch signaling by ubiquitinating the Notch receptors, thereby facilitating their endocytosis. This protein may also promote the ubiquitination and degradation of death-associated protein kinase 1 (DAPK1). [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:21086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21086) · Entrez [57534](https://www.ncbi.nlm.nih.gov/gene/57534) · UniProt [Q86YT6](https://www.uniprot.org/uniprotkb/Q86YT6) · Ensembl [ENSG00000101752](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101752)

## Data

Gene col 2170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2170); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2170]; `tensor/DDL_lfc|DDL_z.npy` [2170]; `embed/gene_vectors.npy` [2170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2170 or target_col == 2170). Every well: [[MIB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
