---
symbol: "HMGB2"
type: "gene"
col: 8868
ensembl_id: "ENSG00000164104"
name: "high mobility group box 2"
location: "4q34.1"
module: 22
arm: "+"
pooled_cpm: 165.47
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HMGB2

*high mobility group box 2* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.98× (z +6.9, q 3e-09, up in 46 of 48 measured lines) ⚠ transcription drop; cell-cycle shift, explains ~62% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.51× (z +5.8, q 6e-07, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.527× (z -6.5, q 4e-08, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNB2]] (+0.75, fdr 7e-06), [[RAD21]] (+0.74, fdr 7e-06), [[NUSAP1]] (+0.71, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | **1.98×** | +6.9 | 3e-09 | 46/48 (HT-29, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.59×** | +6.6 | 1e-08 | 32/48 (SW1417, A549, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.91×** | +6.5 | 1e-08 | 36/49 (PANC-1, A-172, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.85×** | +6.2 | 9e-08 | 35/48 (KATO III, PANC-1, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.8 | 6e-07 | 36/49 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.58×** | +4.6 | 4e-04 | 30/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **2.20×** | +4.2 | 0.002 | 37/47 (AsPC-1, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.53×** | +4.1 | 0.002 | 28/48 (AsPC-1, J82, …) | rises with dose | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.003 | 34/50 (RKO, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | **1.47×** | +3.7 | 0.012 | 27/44 (PANC-1, NCI-H1573, …) | two highest doses | composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.018 | 36/48 (HepG2/C3A, AsPC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.38×** | +3.2 | 0.055 | 25/48 (H4, C32, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.37×** | +3.2 | 0.059 | 26/48 (H4, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~78% of this change | **1.37×** | +3.1 | 0.087 | 25/47 (NCI-H23, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -6.5 | 4e-08 | 45/48 (Panc 03.27, AsPC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.529×** | -6.4 | 4e-08 | 46/48 (NCI-H2347, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.553×** | -6.0 | 4e-07 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.584×** | -5.4 | 8e-06 | 38/48 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.595×** | -4.9 | 9e-05 | 37/48 (SW48, LS 180, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.487×** | -3.8 | 0.014 | 35/48 (BT-474, AN3 CA, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.499×** | -3.7 | 0.020 | 30/47 (Hs 766T, LS 180, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | **0.779×** | -3.6 | 0.026 | 35/49 (NCI-H2347, SW1417, …) | top dose only | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.716×** | -3.4 | 0.047 | 35/48 (C-33 A, SW48, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.719×** | -3.3 | 0.049 | 31/48 (HCT15, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.798×** | -3.2 | 0.066 | 28/49 (BT-474, LoVo, …) | top dose only | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | 0.559× | -3.1 | 0.10 | 29/48 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 0.732× | -3.0 | 0.11 | 26/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.94 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 147 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | [[Panobinostat (drug)]] 5 µM 0.367× (z -9.0) |
| [[KATO III (line)]] | alt | 199 | 4 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.50× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[AsPC-1 (line)]] | alt | 123 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +11.7) | [[Auranofin (drug)]] 5 µM 0.340× (z -8.9) |
| [[J82 (line)]] | alt | 302 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -8.5) |
| [[LS 180 (line)]] | wt | 152 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.242× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.398× (z -8.9) |
| [[SW48 (line)]] | wt | 217 | 0 | 3 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.223× (z -9.9) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.400× (z -8.6) |
| [[A549 (line)]] | wt | 79.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 226 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.3) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.328× (z -9.4) |
| [[SNU-1 (line)]] | wt | 148 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 246 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 166 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[A498 (line)]] | wt | 184 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -8.5) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 119 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 58.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 170 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 4.14× (z +10.6) ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[LOX-IMVI (line)]] | wt | 94.0 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.254× (z -9.1) ⚠ cell-cycle shift, explains ~80% of this change |
| [[NCI-H1573 (line)]] | alt | 48.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change | — |
| [[NCI-H23 (line)]] | alt | 106 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.49× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | — |
| [[NCI-H2347 (line)]] | alt | 455 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.326× (z -9.3) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 191 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0728× (z -11.1) |
| [[SW 900 (line)]] | alt | 80.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 230 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | — |
| [[A-427 (line)]] | wt | 146 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 328 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 254 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 263 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 91.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 179 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 79.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 127 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 171 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 134 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 74.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 339 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 184 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNB2]] | +0.75 | +0.79 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 469 |
| [[RAD21]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[NUSAP1]] | +0.71 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[NEK2]] | +0.71 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[STMN1]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CDK1]] | +0.69 | +0.78 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 526 |
| [[NUF2]] | +0.68 | +0.77 / +0.73 | both halves | 7e-06 |  |
| [[CDC25C]] | +0.68 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[TPX2]] | +0.68 | +0.78 / +0.63 | both halves | 7e-06 |  |
| [[KIF20A]] | +0.67 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[AURKA]] | +0.67 | +0.72 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[NDC80]] | +0.67 | +0.74 / +0.65 | both halves | 7e-06 | STRING 430 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-40.6, -54.7); signed map (-51.2, -46.3). **Vector** length 142, 59.5% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.54 to 60); *DREAM G2/M down* (control, mean cos +0.62 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.53 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.5 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +1.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~62% of this change | +4.4 | +6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.1 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | -0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.7 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.7 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.1 | -6.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | -7.2 | -4.9 |
|  | [[EX229 (drug)]] 5 µM |  | -5.8 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -1.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | -5.4 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group box 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.1 — chr4:173,331,376-173,334,432 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HMG2 |
| Gene groups (HGNC) | Canonical high mobility group; SET complex |
| Hallmark sets | APOPTOSIS, E2F_TARGETS |
| Reactome | 4 pathways, smallest: Apoptosis induced DNA fragmentation; Apoptotic execution phase; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P26583](https://www.uniprot.org/uniprotkb/P26583) (High mobility group protein B2):

> Multifunctional protein with various roles in different cellular compartments. May act in a redox sensitive manner. In the nucleus is an abundant chromatin-associated non-histone protein involved in transcription, chromatin remodeling and V(D)J recombination and probably other processes. Binds DNA with a preference to non-canonical DNA structures such as single-stranded DNA. Can bent DNA and enhance DNA flexibility by looping thus providing a mechanism to promote activities on various gene …

**Summary**, from NCBI Gene [3148](https://www.ncbi.nlm.nih.gov/gene/3148):

> This gene encodes a member of the non-histone chromosomal high mobility group protein family. The proteins of this family are chromatin-associated and ubiquitously distributed in the nucleus of higher eukaryotic cells. In vitro studies have demonstrated that this protein is able to efficiently bend DNA and form DNA circles. These studies suggest a role in facilitating cooperative interactions between cis-acting proteins by promoting DNA flexibility. This protein was also reported to be involved …

**Accessions** — [HGNC:5000](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5000) · Entrez [3148](https://www.ncbi.nlm.nih.gov/gene/3148) · UniProt [P26583](https://www.uniprot.org/uniprotkb/P26583) · Ensembl [ENSG00000164104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164104)

## Data

Gene col 8868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8868); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8868]; `tensor/DDL_lfc|DDL_z.npy` [8868]; `embed/gene_vectors.npy` [8868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8868 or target_col == 8868). Every well: [[HMGB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
