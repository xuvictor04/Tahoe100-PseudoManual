---
symbol: "PYGO2"
type: "gene"
col: 8673
ensembl_id: "ENSG00000163348"
name: "pygopus family PHD finger 2"
location: "1q21.3"
module: 21
arm: "+"
pooled_cpm: 11.55
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PYGO2

*pygopus family PHD finger 2* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.77× (z +7.0, q 1e-09, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.526× (z -7.6, q 2e-11, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRC2A]] (+0.61, fdr 7e-06), [[SHC1]] (+0.59, fdr 1e-05, ⚠ same locus), [[TXLNA]] (+0.59, fdr 3e-05), [[H2AX]] (+0.57, fdr 1e-05); moves opposite to [[NSA2]] (-0.65, fdr 1e-05), [[KIZ-AS1]] (-0.61, fdr 1e-05, ⚠ KIZ-AS1 in the vector space only through flagged drug-doses), [[BIRC6-AS2-1]] (-0.60, fdr 1e-05), [[FAM217A]] (-0.59, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8673.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.77×** | +7.0 | 1e-09 | 30/47 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +6.7 | 6e-09 | 23/41 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.50×** | +5.0 | 1e-04 | 25/47 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.0 | 0.007 | 1/48 (NCI-H1573) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +3.9 | 0.009 | 13/47 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.016 | 13/46 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.5 | 0.041 | 16/40 (KATO III, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.31×** | +3.3 | 0.063 | 5/47 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.063 | 12/44 (LOX-IMVI, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Loperamide (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.087 | 10/46 (LoVo, SW1417, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.087 | 7/48 (SHP-77, A-172, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.096 | 13/46 (A-172, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | 1.29× | +3.0 | 0.10 | 11/46 (LS 180, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8673.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.526×** | -7.6 | 2e-11 | 34/44 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.625×** | -5.9 | 1e-06 | 28/47 (H4, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.454×** | -5.1 | 5e-05 | 22/46 (LoVo, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.740×** | -3.8 | 0.024 | 13/47 (LS 180, NCI-H23, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.766×** | -3.3 | 0.089 | 15/46 (J82, HOP62, …) | rises with dose | position effect removed |
| [[Cyclosporin A (drug)]] 5 µM |  | **0.771×** | -3.3 | 0.089 | 15/47 (A-172, A549, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.772×** | -3.2 | 0.089 | 15/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.610×** | -3.2 | 0.089 | 16/35 (A-427, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.782× | -3.1 | 0.13 | 17/47 (KATO III, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8673. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0864× (z -14.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 6.58 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0985× (z -9.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.9 | 0 | 1 | — | [[ULK-101 (drug)]] 5 µM 0.0537× (z -8.8) |
| [[KATO III (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -9.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.116× (z -9.1) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.49 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8673), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC2A]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SHC1]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TXLNA]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[H2AX]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 | pathway: Formation of the beta-catenin:TCF transactivating complex; STRING 572 |
| [[PLAGL2]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[THOC6]] | +0.55 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[ZNF816]] | +0.55 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PTBP1]] | +0.55 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ZBTB9]] | +0.55 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[CHAMP1]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[CTDSP1]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[ZNF574]] | +0.53 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[APEH]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSA2]] | -0.65 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[KIZ-AS1]] ⚠ | -0.61 | -0.59 / -0.51 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[BIRC6-AS2-1]] | -0.60 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[FAM217A]] | -0.59 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RHOQ-AS1]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[NPEPPS]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZBTB47-AS1]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[TBCA]] | -0.56 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[EFCAB14-AS1]] | -0.55 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ADGRL3-AS1]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.55 | -0.34 / -0.48 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL34]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[ZBTB20-AS5]] | -0.54 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[RPS12]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises PYGO2's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction -0.497). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-54.9, -8.7); signed map (-8.7, -38.6). **Vector** length 67.1, 10.6% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.9 | +4.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +1.9 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +1.6 | +1.8 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -4.2 | -7.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | -3.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -2.9 | -3.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | pygopus family PHD finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:154,957,026-154,963,853 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | PHD finger proteins; Wnt enhanceosome complex |
| Reactome | 4 pathways, smallest: Deactivation of the beta-catenin transactivating complex; Formation of the beta-catenin:TCF transactivating complex; TCF dependent signaling in response to WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRQ0](https://www.uniprot.org/uniprotkb/Q9BRQ0) (Pygopus homolog 2):

> Involved in signal transduction through the Wnt pathway.

**Summary**, from NCBI Gene [90780](https://www.ncbi.nlm.nih.gov/gene/90780):

> Predicted to enable chromatin binding activity; histone acetyltransferase regulator activity; and histone binding activity. Predicted to be involved in Wnt signaling pathway. Predicted to act upstream of or within several processes, including canonical Wnt signaling pathway; lens development in camera-type eye; and spermatid nucleus differentiation. Located in nucleoplasm. Part of beta-catenin-TCF complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30257](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30257) · Entrez [90780](https://www.ncbi.nlm.nih.gov/gene/90780) · UniProt [Q9BRQ0](https://www.uniprot.org/uniprotkb/Q9BRQ0) · Ensembl [ENSG00000163348](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163348)

## Data

Gene col 8673: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8673); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8673, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8673]; `tensor/DDL_lfc|DDL_z.npy` [8673]; `embed/gene_vectors.npy` [8673]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8673 or target_col == 8673). Every well: [[PYGO2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYGO2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
