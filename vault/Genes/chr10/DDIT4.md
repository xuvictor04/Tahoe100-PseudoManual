---
symbol: "DDIT4"
type: "gene"
col: 9610
ensembl_id: "ENSG00000168209"
name: "DNA damage inducible transcript 4"
location: "10q22.1"
module: 79
arm: "+"
pooled_cpm: 195.29
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# DDIT4

*DNA damage inducible transcript 4* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.48× (z +5.0, q 3e-04, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.290× (z -11.2, q 3e-26, down in 40 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HILPDA]] (+0.72, fdr 7e-06), [[MKNK2]] (+0.70, fdr 8e-06), [[RLF]] (+0.68, fdr 1e-05); moves opposite to [[PARVA]] (-0.65, fdr 1e-05), [[AVEN]] (-0.62, fdr 1e-05), [[RBM12]] (-0.60, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[ADM]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.48×** | +5.0 | 3e-04 | 41/46 (C32, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM |  | **1.69×** | +4.8 | 5e-04 | 42/45 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.92×** | +3.6 | 0.063 | 35/45 (CFPAC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.4 | 0.094 | 26/44 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.66× | +3.2 | 0.12 | 26/45 (A549, C32, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.65× | +3.2 | 0.12 | 34/45 (Hs 766T, SNU-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | 2.49× | +3.0 | 0.19 | 35/45 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9610.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.290×** | -11.2 | 3e-26 | 40/45 (NCI-H2347, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.357×** | -9.3 | 4e-18 | 42/46 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.264×** | -8.2 | 5e-14 | 40/42 (NCI-H2347, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.332×** | -6.8 | 2e-09 | 41/45 (C32, H4, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.356×** | -6.3 | 3e-08 | 33/45 (AN3 CA, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.504×** | -6.2 | 6e-08 | 44/45 (AN3 CA, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.389×** | -6.0 | 1e-07 | 37/46 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.416×** | -5.6 | 2e-06 | 31/45 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.426×** | -5.4 | 3e-06 | 41/45 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.433×** | -5.3 | 5e-06 | 42/45 (CFPAC-1, SW 900, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.419×** | -5.3 | 5e-06 | 37/47 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.448×** | -4.7 | 1e-04 | 31/42 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.481×** | -4.7 | 1e-04 | 36/45 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.496×** | -4.5 | 3e-04 | 40/45 (KATO III, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.500×** | -4.2 | 8e-04 | 34/44 (SW48, PANC-1, …) | two highest doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.583×** | -3.4 | 0.020 | 38/46 (SW48, A-172, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | **0.512×** | -3.0 | 0.070 | 34/45 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.58 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 338 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 5.60× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 272 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0941× (z -25.3) |
| [[PANC-1 (line)]] | alt | 244 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -18.5) |
| [[HCT15 (line)]] | alt | 326 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0555× (z -22.9) |
| [[AN3 CA (line)]] | alt | 307 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -15.9) |
| [[H4 (line)]] | wt | 260 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -12.5) |
| [[KATO III (line)]] | alt | 181 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -12.5) |
| [[LoVo (line)]] | wt | 180 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.159× (z -10.5) |
| [[LS 180 (line)]] | wt | 216 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0437× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.120× (z -11.8) |
| [[SW 900 (line)]] | alt | 195 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.8) |
| [[A-172 (line)]] | wt | 178 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -15.7) |
| [[A498 (line)]] | wt | 425 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -13.2) |
| [[A549 (line)]] | wt | 212 | 2 | 1 | [[Harringtonine (drug)]] 0.5 µM 5.61× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -9.9) |
| [[BT-474 (line)]] | alt | 58.8 | 1 | 2 (1 ⚠) | [[Artesunate (drug)]] 5 µM 3.50× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 347 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 213 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -10.4) |
| [[HS-578T (line)]] | alt | 204 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -15.1) |
| [[LOX-IMVI (line)]] | wt | 175 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 102 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0652× (z -24.7) |
| [[NCI-H460 (line)]] | wt | 272 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 5.95× (z +10.3) ⚠ cell-cycle shift, explains ~45% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 286 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.245× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 257 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -15.6) |
| [[SNU-1 (line)]] | wt | 121 | 2 | 1 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 9.72× (z +14.4) | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.8) |
| [[CHP-212 (line)]] | wt | 235 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0362× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.175× (z -10.6) |
| [[HOP62 (line)]] | alt | 266 | 0 | 2 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.225× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 159 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 200 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -14.4) |
| [[SNU-423 (line)]] | alt | 172 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -11.0) |
| [[SW48 (line)]] | wt | 211 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0440× (z -11.9) |
| [[SW480 (line)]] | alt | 156 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0984× (z -10.9) |
| [[C-33 A (line)]] | alt | 52.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 352 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0985× (z -10.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -9.8) |
| [[HT-29 (line)]] | alt | 103 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.175× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 161 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 158 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.2) |
| [[NCI-H661 (line)]] | alt | 166 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0948× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 82.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 251 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -10.9) |
| [[A-427 (line)]] | wt | 33.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.9 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 39.7 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HILPDA]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[MKNK2]] | +0.70 | +0.57 / +0.67 | both halves | 8e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[RLF]] | +0.68 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FAM13A]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.67 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[HERPUD1]] | +0.67 | +0.62 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[FAM162A]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[ADM]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[UBE2Q2P2]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[KDM3A]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[RAB20]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARVA]] | -0.65 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[AVEN]] | -0.62 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[RBM12]] | -0.60 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.60 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[WSB2]] | -0.55 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[TRIP12]] | -0.55 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[ARMC6]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[EXOC7]] | -0.54 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[PBLD]] | -0.54 | -0.64 / -0.42 | both halves | 4e-05 |  |
| [[ELK4]] | -0.54 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ANAPC7]] | -0.53 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[VPS52]] | -0.53 | -0.29 / -0.55 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DDIT4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADM]] | B | ADM activity raises DDIT4's level | lines that do not express ADM (6) vs lines expressing it (44) | 2.55× lower at baseline in the lines without ADM | 0.060 | ⚠ within organs, on part of the lines; also absent: FTH1, CDC42EP1, ENSG00000284716; its own permutation p |
| [[PPP1R3C]] | B | PPP1R3C activity raises DDIT4's level | lines that do not express PPP1R3C (22) vs lines expressing it (28) | 1.35× lower at baseline in the lines without PPP1R3C | 0.083 | ⚠ within organs, on part of the lines; also absent: CDH2, SSTR2, IDO1 |
| [[CDON]] | C | CDON activity raises DDIT4's level | lines that do not express CDON (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without CDON | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; its own permutation p |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADM]] | C | DDIT4 activity raises ADM's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 3.84× lower at baseline in the lines without DDIT4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |
| [[ARMC6]] | C | DDIT4 activity lowers ARMC6's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 1.73× higher at baseline in the lines without DDIT4 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |
| [[AVPI1]] | C | DDIT4 activity raises AVPI1's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 2.83× lower at baseline in the lines without DDIT4 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent |
| [[PARVA]] | C | DDIT4 activity raises PARVA's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 4.15× lower at baseline in the lines without DDIT4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |
| [[ARL6]] | C | DDIT4 activity lowers ARL6's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 1.94× higher at baseline in the lines without DDIT4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |
| [[CLK3]] | C | DDIT4 activity raises CLK3's level | lines that do not express DDIT4 (3) vs lines expressing it (47) | 1.37× lower at baseline in the lines without DDIT4 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, TIMP1, UGDH; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, -13.8); signed map (-33.4, 24.3). **Vector** length 142, 56.7% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.57 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +1.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | +2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.8 | -2.6 |
|  | [[Artesunate (drug)]] 5 µM |  | +5.7 | +4.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | -5.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.7 | +3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.3 | +2.2 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.5 | -8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.1 | -6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.2 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -11.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.7 | -6.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.3 | -3.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.7 | -2.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.7 | -1.9 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DNA damage inducible transcript 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:72,273,919-72,276,036 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RTP801, FLJ20500, REDD-1, REDD1, Dig2 |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, GLYCOLYSIS, HYPOXIA, P53_PATHWAY, MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: TP53 Regulates Metabolic Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NX09](https://www.uniprot.org/uniprotkb/Q9NX09) (DNA damage-inducible transcript 4 protein):

> Regulates cell growth, proliferation and survival via inhibition of the activity of the mammalian target of rapamycin complex 1 (mTORC1). Inhibition of mTORC1 is mediated by a pathway that involves DDIT4/REDD1, AKT1, the TSC1-TSC2 complex and the GTPase RHEB. Plays an important role in responses to cellular energy levels and cellular stress, including responses to hypoxia and DNA damage. Regulates p53/TP53-mediated apoptosis in response to DNA damage via its effect on mTORC1 activity. Its role …

**Summary**, from NCBI Gene [54541](https://www.ncbi.nlm.nih.gov/gene/54541):

> Predicted to enable 14-3-3 protein binding activity. Involved in negative regulation of TOR signaling and response to hypoxia. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24944) · Entrez [54541](https://www.ncbi.nlm.nih.gov/gene/54541) · UniProt [Q9NX09](https://www.uniprot.org/uniprotkb/Q9NX09) · Ensembl [ENSG00000168209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168209)

## Data

Gene col 9610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9610); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9610]; `tensor/DDL_lfc|DDL_z.npy` [9610]; `embed/gene_vectors.npy` [9610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9610 or target_col == 9610). Every well: [[DDIT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDIT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
