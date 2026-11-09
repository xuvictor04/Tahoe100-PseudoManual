---
symbol: "APEX2"
type: "gene"
col: 9768
ensembl_id: "ENSG00000169188"
name: "apurinic/apyrimidinic endodeoxyribonuclease 2"
location: "Xp11.21"
module: 21
arm: "+"
pooled_cpm: 8.05
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# APEX2

*apurinic/apyrimidinic endodeoxyribonuclease 2* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.70× (z +7.6, q 2e-11, up in 27 of 45 measured lines) ⚠ cell-cycle shift, explains ~54% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.36× (z +6.3, q 4e-08, up in 20 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.583× (z -7.8, q 4e-12, down in 22 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEMIN4]] (+0.69, fdr 7e-06), [[C19orf48]] (+0.66, fdr 7e-06), [[TBRG4]] (+0.65, fdr 7e-06); moves opposite to [[FLJ40194]] (-0.65, fdr 1e-05), [[ZBTB47-AS1]] (-0.60, fdr 1e-05), [[DMXL1-DT]] (-0.58, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9768.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.70×** | +7.6 | 2e-11 | 27/45 (HOP62, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.65×** | +7.2 | 2e-10 | 28/47 (HOP62, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.58×** | +6.6 | 7e-09 | 17/46 (HOP62, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.3 | 4e-08 | 20/47 (J82, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +5.9 | 5e-07 | 17/45 (NCI-H1792, KATO III, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.47×** | +5.6 | 2e-06 | 15/46 (J82, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.39×** | +4.6 | 4e-04 | 15/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | **1.36×** | +4.3 | 0.001 | 2/13 (HS-578T, HOP62) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.2 | 0.002 | 11/45 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +4.1 | 0.002 | 10/42 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +3.5 | 0.025 | 9/38 (A549, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.27×** | +3.3 | 0.042 | 9/39 (PANC-1, J82, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.044 | 1/43 (MIA PaCa-2) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9768.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -7.8 | 4e-12 | 22/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -7.5 | 3e-11 | 24/41 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.723×** | -6.6 | 8e-09 | 25/41 (SW48, SW480, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.468×** | -5.7 | 2e-06 | 14/42 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.740×** | -4.3 | 0.002 | 15/45 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.583×** | -4.1 | 0.005 | 13/40 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.757×** | -4.0 | 0.005 | 14/47 (RPMI-7951, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.785×** | -3.5 | 0.036 | 14/45 (LoVo, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.779×** | -3.4 | 0.044 | 6/44 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.810× | -3.0 | 0.13 | 8/42 (Panc 03.27, COLO 205, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9768. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 10.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -9.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0922× (z -10.2) |
| [[SW480 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -9.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-427 (line)]] | wt | 10.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 6.21 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.1000× (z -9.7) |
| [[BT-474 (line)]] | alt | 6.89 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0711× (z -9.7) |
| [[H4 (line)]] | wt | 10.1 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0747× (z -9.4) |
| [[HS-578T (line)]] | alt | 3.95 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0612× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 6.94 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0926× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 3.41 | 0 | 1 | — | [[Entrectinib (drug)]] 5 µM 0.0837× (z -8.6) |
| [[SW48 (line)]] | wt | 5.78 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0823× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9768), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEMIN4]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[C19orf48]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TBRG4]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[TUBG1]] | +0.63 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[PRPF4]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[EXOSC2]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 | pathway: Affinity selection of immunoglobulins |
| [[FEN1]] | +0.57 | +0.54 / +0.61 | both halves | 1e-05 | STRING 758 |
| [[DCLRE1B]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[XRCC3]] | +0.56 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ALDH1B1]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[CHMP7]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[ZBTB9]] | +0.55 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLJ40194]] | -0.65 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[ZBTB47-AS1]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[DMXL1-DT]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[LRRC37A16P]] | -0.57 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[CNGB3]] | -0.56 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[ERP29]] | -0.56 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[USF2]] | -0.55 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[HSPA2-AS1]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[SMDT1]] | -0.54 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[YY1]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[NME9]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[DNAJC27-AS1]] | -0.52 | -0.40 / -0.60 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction -0.514). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.6, -45.1); signed map (-32.5, -50.6). **Vector** length 61.6, 8.85% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +5.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +3.5 | +5.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.4 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | +2.7 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.6 | +6.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.0 | +2.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.3 | -6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | apurinic/apyrimidinic endodeoxyribonuclease 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:55,000,363-55,009,057 (+) |
| Ensembl biotype | protein_coding |
| Also known as | APEXL2, APE2, XTH2, ZGRF2 |
| Gene groups (HGNC) | Zinc fingers GRF-type |
| Reactome | 5 pathways, smallest: Somatic hypermutation of immunoglobulin genes by error-prone base excision repair (BER); Somatic hypermutation of immunoglobulin genes; Affinity selection of immunoglobulins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBZ4](https://www.uniprot.org/uniprotkb/Q9UBZ4) (DNA-(apurinic or apyrimidinic site) endonuclease 2):

> Functions as a weak apurinic/apyrimidinic (AP) endodeoxyribonuclease in the DNA base excision repair (BER) pathway of DNA lesions induced by oxidative and alkylating agents. Initiates repair of AP sites in DNA by catalyzing hydrolytic incision of the phosphodiester backbone immediately adjacent to the damage, generating a single-strand break with 5'-deoxyribose phosphate and 3'-hydroxyl ends. Also displays double-stranded DNA 3'-5' exonuclease, 3'-phosphodiesterase activities. Shows robust …

**Summary**, from NCBI Gene [27301](https://www.ncbi.nlm.nih.gov/gene/27301):

> Apurinic/apyrimidinic (AP) sites occur frequently in DNA molecules by spontaneous hydrolysis, by DNA damaging agents or by DNA glycosylases that remove specific abnormal bases. AP sites are pre-mutagenic lesions that can prevent normal DNA replication so the cell contains systems to identify and repair such sites. Class II AP endonucleases cleave the phosphodiester backbone 5' to the AP site. This gene encodes a protein shown to have a weak class II AP endonuclease activity. Most of the encoded …

**Accessions** — [HGNC:17889](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17889) · Entrez [27301](https://www.ncbi.nlm.nih.gov/gene/27301) · UniProt [Q9UBZ4](https://www.uniprot.org/uniprotkb/Q9UBZ4) · Ensembl [ENSG00000169188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169188)

## Data

Gene col 9768: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9768); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9768, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9768]; `tensor/DDL_lfc|DDL_z.npy` [9768]; `embed/gene_vectors.npy` [9768]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9768 or target_col == 9768). Every well: [[APEX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APEX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
