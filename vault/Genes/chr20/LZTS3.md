---
symbol: "LZTS3"
type: "gene"
col: 1553
ensembl_id: "ENSG00000088899"
name: "leucine zipper tumor suppressor family member 3"
location: "20p13"
module: 2
arm: "+"
pooled_cpm: 4.88
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# LZTS3

*leucine zipper tumor suppressor family member 3* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.03× (z +7.9, q 2e-12, up in 30 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.319× (z -6.7, q 2e-08, down in 23 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHC2]] (+0.64, fdr 7e-06), [[ARVCF]] (+0.64, fdr 2e-05), [[MAPK8IP1]] (+0.62, fdr 1e-05); moves opposite to [[SRBD1]] (-0.49, fdr 5e-05), [[TFAM]] (-0.46, fdr 1e-04), [[SCGB2B2]] (-0.46, fdr 0.003, ⚠ not reproduced), [[LINC01515]] (-0.46, fdr 5e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[RHOB]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1553.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +7.9 | 2e-12 | 30/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.01×** | +7.8 | 2e-12 | 29/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +6.9 | 1e-09 | 23/41 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.8 | 1e-09 | 7/9 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.63×** | +5.4 | 6e-06 | 16/40 (RKO, A-172, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.66×** | +5.4 | 7e-06 | 18/43 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +4.9 | 8e-05 | 4/14 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.6 | 3e-04 | 9/24 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.33×** | +4.4 | 5e-04 | 15/45 (HT-29, HepG2/C3A, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.47×** | +4.2 | 0.001 | 14/47 (HepG2/C3A, LoVo, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.71×** | +4.2 | 0.001 | 4/30 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.002 | 12/47 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.003 | 12/44 (MIA PaCa-2, RKO, …) | rises with dose | low cells (technical?); position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.8 | 0.005 | 3/45 (HS-578T, NCI-H2347, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.011 | 10/46 (HT-29, SHP-77, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.56×** | +3.5 | 0.013 | 6/40 (CFPAC-1, LoVo, …) | rises with dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.017 | 4/48 (NCI-H460, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.020 | 7/47 (NCI-H460, A-172, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.79×** | +3.4 | 0.020 | 4/29 (A-172, HT-29, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.319×** | -6.7 | 2e-08 | 23/36 (AsPC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.611×** | -5.5 | 1e-05 | 17/39 (AsPC-1, HT-29, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -4.8 | 3e-04 | 16/44 (MIA PaCa-2, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -4.7 | 4e-04 | 16/38 (COLO 205, PANC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.696×** | -4.0 | 0.006 | 19/41 (SW1417, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.698×** | -4.0 | 0.006 | 10/47 (CFPAC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.730×** | -3.5 | 0.036 | 11/46 (SW1417, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | **0.809×** | -3.4 | 0.055 | 10/48 (J82, KATO III, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.751×** | -3.2 | 0.085 | 10/44 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.750× | -3.1 | 0.11 | 13/37 (HS-578T, MIA PaCa-2, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.760× | -3.1 | 0.11 | 8/47 (LoVo, SNU-423, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.763× | -3.0 | 0.12 | 14/45 (COLO 205, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 9.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 4.75 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0629× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 3.89 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.5 µM 0.105× (z -8.5) |
| [[COLO 205 (line)]] | alt | 7.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0669× (z -9.4) |
| [[HOP62 (line)]] | alt | 3.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +8.6) | — |
| [[KATO III (line)]] | alt | 5.18 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0659× (z -9.9) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SHP-77 (line)]] | alt | 5.90 | 0 | 1 | — | [[8-Hydroxyquinoline (drug)]] 0.05 µM 0.0634× (z -9.3) |
| [[SW1417 (line)]] | alt | 4.81 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0832× (z -9.5) |
| [[A-427 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHC2]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ARVCF]] | +0.64 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[MAPK8IP1]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[DUSP8]] | +0.59 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[FADS3]] | +0.57 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[GDI1]] | +0.57 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[PNPLA6]] | +0.57 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[ZDHHC18]] | +0.56 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[EEF1A2]] | +0.56 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[PPP1R12C]] | +0.56 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[KIF1A]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[CFAP410]] | +0.55 | +0.46 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRBD1]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[TFAM]] | -0.46 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[SCGB2B2]] | -0.46 | -0.09 / -0.44 | ⚠ not reproduced | 0.003 |  |
| [[LINC01515]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RHOB]] | C | LZTS3's natural level strengthens RHOB's drug response | LZTS3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.13; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | LZTS3's natural level raises the cells' numbers under Bendamustine 0.5 µM (protects the cells) | LZTS3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.57 | 0.505 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (19.9, -1.4); signed map (-3.8, 23.9). **Vector** length 65.6, 9.40% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +4.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +6.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.2 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.1 | +5.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +4.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +3.6 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.9 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.7 | -1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.5 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | leucine zipper tumor suppressor family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,162,617-3,173,549 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ProSAPiP1, KIAA0552 |
| Gene groups (HGNC) | Leucine zipper tumor suppressor family |
| Matched by | ensembl_id |

**Function**, from UniProt [O60299](https://www.uniprot.org/uniprotkb/O60299) (Leucine zipper putative tumor suppressor 3):

> May be involved in promoting the maturation of dendritic spines, probably via regulating SIPA1L1 levels at the postsynaptic density of synapses.

**Summary**, from NCBI Gene [9762](https://www.ncbi.nlm.nih.gov/gene/9762):

> Predicted to enable PDZ domain binding activity. Predicted to be involved in protein homooligomerization; regulation of dendritic spine morphogenesis; and regulation of postsynapse assembly. Predicted to be located in postsynaptic density. Predicted to be active in dendritic spine and glutamatergic synapse. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30139) · Entrez [9762](https://www.ncbi.nlm.nih.gov/gene/9762) · UniProt [O60299](https://www.uniprot.org/uniprotkb/O60299) · Ensembl [ENSG00000088899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000088899)

## Data

Gene col 1553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1553); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1553]; `tensor/DDL_lfc|DDL_z.npy` [1553]; `embed/gene_vectors.npy` [1553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1553 or target_col == 1553). Every well: [[LZTS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LZTS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
