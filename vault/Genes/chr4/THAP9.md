---
symbol: "THAP9"
type: "gene"
col: 9606
ensembl_id: "ENSG00000168152"
name: "THAP domain containing 9"
location: "4q21.22"
module: 77
arm: "-"
pooled_cpm: 9.74
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# THAP9

*THAP domain containing 9* — 4q21.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.55× (z +19.5, q 0e+00, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 0.533× (z -9.3, q 6e-18, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CGGBP1]] (+0.76, fdr 7e-06), [[HHLA3]] (+0.71, fdr 4e-05), [[THAP2]] (+0.67, fdr 1e-04); moves opposite to [[PACC1]] (-0.66, fdr 2e-05), [[LPCAT4]] (-0.65, fdr 4e-05), [[ANKRD27]] (-0.65, fdr 3e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRR5]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +19.5 | 0e+00 | 41/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +12.5 | 2e-33 | 35/43 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.99×** | +10.2 | 5e-22 | 30/42 (LS 180, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +10.1 | 7e-22 | 35/46 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.5 | 4e-06 | 19/45 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.6 | 4e-04 | 20/46 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.44×** | +4.5 | 7e-04 | 14/26 (SW480, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.032 | 12/47 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.065 | 6/47 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.13 | 12/46 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **0.533×** | -9.3 | 6e-18 | 35/45 (BT-474, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.735×** | -4.6 | 0.001 | 17/47 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **0.758×** | -4.1 | 0.006 | 15/44 (SK-MEL-2, LS 180, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.681×** | -4.1 | 0.006 | 8/44 (HCT15, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.785×** | -3.6 | 0.035 | 11/47 (CHP-212, SW 900, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.718×** | -3.5 | 0.040 | 10/42 (SW480, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.785×** | -3.5 | 0.041 | 12/45 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Drospirenone (drug)]] 0.5 µM |  | 0.816× | -3.0 | 0.15 | 7/45 (BT-474, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | 0.809× | -3.0 | 0.15 | 8/17 (SW480, LoVo, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.67 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +8.6) | [[Pimozide (drug)]] 0.5 µM 0.0761× (z -12.5) ⚠ transcription drop · without an alert: [[Monocrotaline (drug)]] 0.05 µM 0.0922× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 8.54 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +8.9) | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0872× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 6.49 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +10.8) | — |
| [[LoVo (line)]] | wt | 13.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[BT-474 (line)]] | alt | 7.39 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.105× (z -9.2) |
| [[C-33 A (line)]] | alt | 14.5 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0770× (z -10.6) |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.114× (z -9.5) |
| [[LS 180 (line)]] | wt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +10.0) | — |
| [[NCI-H1573 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 6.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +9.7) | — |
| [[NCI-H2347 (line)]] | alt | 6.99 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.107× (z -11.4) ⚠ transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H460 (line)]] | wt | 8.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.9) | — |
| [[RKO (line)]] | wt | 9.71 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0739× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.152× (z -9.1) |
| [[SW480 (line)]] | alt | 9.76 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.178× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[A-427 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CGGBP1]] | +0.76 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[HHLA3]] | +0.71 | +0.77 / +0.42 | both halves | 4e-05 |  |
| [[THAP2]] | +0.67 | +0.70 / +0.35 | both halves | 1e-04 | same gene group |
| [[TAF9]] | +0.66 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[SMIM19]] | +0.66 | +0.66 / +0.37 | both halves | 8e-05 |  |
| [[PAN2]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[F8]] | +0.65 | +0.62 / +0.39 | both halves | 6e-05 |  |
| [[EP300]] | +0.64 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[NDUFA6-DT]] | +0.64 | +0.70 / +0.32 | both halves | 2e-04 |  |
| [[ZC3H6]] | +0.64 | +0.76 / +0.41 | both halves | 4e-05 |  |
| [[DDX6]] | +0.64 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[PRKAR1A]] | +0.63 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PACC1]] | -0.66 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[LPCAT4]] | -0.65 | -0.65 / -0.41 | both halves | 4e-05 |  |
| [[ANKRD27]] | -0.65 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[TMEM120B]] | -0.65 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[GFOD2]] | -0.64 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[ST6GALNAC4]] | -0.64 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[BICD2]] | -0.64 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[TRABD]] | -0.63 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[CTNNBL1]] | -0.62 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[WASF3]] | -0.62 | -0.60 / -0.27 | both halves | 3e-04 |  |
| [[CMTM8]] | -0.61 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SRPK2]] | -0.61 | -0.66 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRR5]] | C | PRR5 activity raises THAP9's level | lines that do not express PRR5 (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without PRR5 | 0.036 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: NECTIN1, PLEKHG3, SNED1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (1.8, 11.8); signed map (21.2, -15.6). **Vector** length 76.1, 13.0% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.1 | +19.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +12.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +10.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.1 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +0.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.0 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.5 | -9.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.1 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.7 | +0.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -2.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.22 — chr4:82,900,684-82,919,969 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34093 |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5L6](https://www.uniprot.org/uniprotkb/Q9H5L6) (DNA transposase THAP9):

> Active transposase that specifically recognizes the bipartite 5'-TXXGGGX(A/T)-3' consensus motif and mediates transposition.

**Summary**, from NCBI Gene [79725](https://www.ncbi.nlm.nih.gov/gene/79725):

> Enables sequence-specific DNA binding activity and transposase activity. Involved in DNA integration and DNA transposition. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23192) · Entrez [79725](https://www.ncbi.nlm.nih.gov/gene/79725) · UniProt [Q9H5L6](https://www.uniprot.org/uniprotkb/Q9H5L6) · Ensembl [ENSG00000168152](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168152)

## Data

Gene col 9606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9606); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9606]; `tensor/DDL_lfc|DDL_z.npy` [9606]; `embed/gene_vectors.npy` [9606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9606 or target_col == 9606). Every well: [[THAP9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
