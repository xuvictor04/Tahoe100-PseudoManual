---
symbol: "GMPS"
type: "gene"
col: 8745
ensembl_id: "ENSG00000163655"
name: "guanosine monophosphate synthase"
location: "3q25.31"
module: 6
arm: "+"
pooled_cpm: 104.95
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# GMPS

*guanosine monophosphate synthase* — 3q25.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.38× (z +7.6, q 2e-11, up in 31 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.51× (z +4.2, q 0.003, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (NCI-H1792 2.62×, NCI-H460 1.91×; ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.27×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.689× (z -13.0, q 6e-36, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSE1L]] (+0.76, fdr 7e-06), [[CEP78]] (+0.76, fdr 7e-06), [[RANBP1]] (+0.74, fdr 7e-06); moves opposite to [[JUND]] (-0.65, fdr 7e-06), [[OFD1]] (-0.65, fdr 7e-06), [[NFKBIL1]] (-0.64, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LAMB1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8745.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 2 lines (NCI-H1792 2.62×, NCI-H460 1.91×; ⚠ unreliable plate only); [[Dinaciclib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 2.27×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +7.6 | 2e-11 | 31/47 (PANC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +6.8 | 3e-09 | 35/48 (NCI-H1792, NCI-H460, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +5.2 | 3e-05 | 23/47 (NCI-H460, H4, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.23×** | +5.1 | 4e-05 | 30/48 (H4, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change | **1.22×** | +4.7 | 3e-04 | 21/44 (MIA PaCa-2, NCI-H1792, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.003 | 22/48 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.19× | +4.1 | 0.004 | 19/48 (A-427, SW48, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 1.16× | +3.7 | 0.016 | 20/49 (MIA PaCa-2, SNU-423, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.16× | +3.6 | 0.016 | 16/48 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.16× | +3.6 | 0.016 | 16/48 (H4, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 1.15× | +3.4 | 0.032 | 19/48 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.15× | +3.4 | 0.038 | 14/48 (PANC-1, MIA PaCa-2, …) | two highest doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.14× | +3.1 | 0.075 | 10/48 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.085 | 5/48 (CFPAC-1, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.13× | +3.1 | 0.085 | 14/48 (H4, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8745.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.689×** | -13.0 | 6e-36 | 36/48 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.741×** | -7.4 | 4e-11 | 35/48 (J82, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.822×** | -6.8 | 2e-09 | 23/48 (A498, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.754×** | -6.7 | 3e-09 | 29/48 (A-427, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.802×** | -5.4 | 6e-06 | 27/48 (J82, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.807×** | -5.3 | 1e-05 | 25/48 (SNU-1, A498, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.824×** | -4.8 | 1e-04 | 25/48 (LOX-IMVI, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.821×** | -4.7 | 2e-04 | 23/48 (A-172, H4, …) | all doses, stronger at high dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.747×** | -4.3 | 0.001 | 22/48 (AsPC-1, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.758×** | -4.1 | 0.003 | 22/48 (SNU-423, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.852× | -4.0 | 0.004 | 9/48 (KATO III, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.854× | -3.9 | 0.005 | 16/49 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.850× | -3.9 | 0.005 | 22/47 (SW 1271, HEC-1-A, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.859× | -3.8 | 0.007 | 13/49 (HOP62, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.856× | -3.6 | 0.014 | 20/47 (hTERT-HPNE, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.877× | -3.2 | 0.042 | 9/48 (J82, HOP62, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | 0.881× | -3.1 | 0.057 | 11/48 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.877× | -3.1 | 0.057 | 14/48 (NCI-H1792, HCT15, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.741×** | -3.0 | 0.068 | 14/47 (LoVo, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.887× | -3.0 | 0.078 | 7/49 (KATO III, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8745. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 252 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.407× (z -14.0) |
| [[SW480 (line)]] | alt | 138 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.655× (z -9.6) |
| [[A-427 (line)]] | wt | 224 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.393× (z -12.4) |
| [[A498 (line)]] | wt | 93.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.532× (z -12.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.573× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 136 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -17.6) |
| [[A-172 (line)]] | wt | 117 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.588× (z -9.4) ⚠ cell-cycle shift, explains ~10% of this change |
| [[AN3 CA (line)]] | alt | 152 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.268× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 53.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -13.1) |
| [[HS-578T (line)]] | alt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.535× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 173 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 55.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.62× (z +9.5) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -14.9) |
| [[NCI-H460 (line)]] | wt | 78.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.91× (z +9.2) ⚠ unreliable plate only | — |
| [[PANC-1 (line)]] | alt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.644× (z -10.2) |
| [[RKO (line)]] | wt | 133 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 123 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.458× (z -9.5) |
| [[SNU-1 (line)]] | wt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -10.1) |
| [[A549 (line)]] | wt | 88.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 125 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 79.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 185 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 61.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 106 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 77.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 93.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 114 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8745), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSE1L]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 | STRING 454 |
| [[CEP78]] | +0.76 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[RANBP1]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.73 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[CDCA7]] | +0.72 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[TFDP1]] | +0.72 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[MCM6]] | +0.71 | +0.69 / +0.70 | both halves | 7e-06 | STRING 555 |
| [[PRPS2]] | +0.71 | +0.67 / +0.72 | both halves | 7e-06 | STRING 627 |
| [[MACROH2A1]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[DSCC1]] | +0.70 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[RBBP7]] | +0.70 | +0.67 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUND]] | -0.65 | -0.71 / -0.62 | both halves | 7e-06 |  |
| [[OFD1]] | -0.65 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[NFKBIL1]] | -0.64 | -0.66 / -0.65 | both halves | 7e-06 |  |
| [[CTR9]] | -0.62 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[PI4KB]] | -0.62 | -0.61 / -0.57 | both halves | 8e-06 |  |
| [[MTHFR]] | -0.61 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[TJAP1]] | -0.61 | -0.70 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB1]] | B | LAMB1 activity lowers GMPS's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 1.64× higher at baseline in the lines without LAMB1 | 0.010 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |
| [[DSCC1]] | C | DSCC1 activity raises GMPS's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without DSCC1 | 0.052 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.707). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-31.0, -41.5); signed map (-32.8, -44.1). **Vector** length 134, 39.9% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.52 to 65); *DNA strand elongation* (reactome, mean cos +0.53 to 28); *DNA Replication* (reactome, mean cos +0.53 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.1 | +7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.3 | +6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +5.0 | +4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.4 | +3.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.4 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.4 | -13.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.5 | -6.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -5.3 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -5.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.6 | -4.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -4.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.2 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | guanosine monophosphate synthase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.31 — chr3:155,870,650-155,944,020 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GATD7 |
| Gene groups (HGNC) | Glutamine amidotransferase class 1 domain containing |
| Hallmark sets | HEME_METABOLISM, MTORC1_SIGNALING |
| Reactome | 5 pathways, smallest: Purine ribonucleoside monophosphate biosynthesis; Nucleotide biosynthesis; Azathioprine ADME |
| Matched by | ensembl_id |

**Function**, from UniProt [P49915](https://www.uniprot.org/uniprotkb/P49915) (GMP synthase):

> Catalyzes the conversion of xanthine monophosphate (XMP) to GMP in the presence of glutamine and ATP through an adenyl-XMP intermediate.

**Summary**, from NCBI Gene [8833](https://www.ncbi.nlm.nih.gov/gene/8833):

> In the de novo synthesis of purine nucleotides, IMP is the branch point metabolite at which point the pathway diverges to the synthesis of either guanine or adenine nucleotides. In the guanine nucleotide pathway, there are 2 enzymes involved in converting IMP to GMP, namely IMP dehydrogenase (IMPD1), which catalyzes the oxidation of IMP to XMP, and GMP synthetase, which catalyzes the amination of XMP to GMP. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4378) · Entrez [8833](https://www.ncbi.nlm.nih.gov/gene/8833) · UniProt [P49915](https://www.uniprot.org/uniprotkb/P49915) · Ensembl [ENSG00000163655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163655)

## Data

Gene col 8745: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8745); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8745, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8745]; `tensor/DDL_lfc|DDL_z.npy` [8745]; `embed/gene_vectors.npy` [8745]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8745 or target_col == 8745). Every well: [[GMPS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GMPS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
