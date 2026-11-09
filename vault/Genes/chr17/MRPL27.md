---
symbol: "MRPL27"
type: "gene"
col: 2999
ensembl_id: "ENSG00000108826"
name: "mitochondrial ribosomal protein L27"
location: "17q21.33"
module: 119
arm: "+"
pooled_cpm: 21.97
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# MRPL27

*mitochondrial ribosomal protein L27* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.70× (z +7.2, q 5e-10, up in 31 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.46× (z +5.3, q 3e-05, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.638× (z -6.1, q 3e-07, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NGDN]] (+0.66, fdr 7e-06), [[AAR2]] (+0.64, fdr 9e-06), [[CCDC12]] (+0.62, fdr 1e-05); moves opposite to [[EPB41L2]] (-0.57, fdr 1e-05), [[STT3B]] (-0.54, fdr 1e-05), [[GNG12]] (-0.54, fdr 1e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2999.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +7.2 | 5e-10 | 31/45 (A-427, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.46×** | +5.3 | 3e-05 | 27/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 3e-05 | 24/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.50×** | +4.8 | 2e-04 | 21/38 (A-172, A498, …) | inconsistent across doses | composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.54×** | +4.3 | 0.002 | 22/46 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +3.6 | 0.036 | 19/48 (A498, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.097 | 8/48 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.25×** | +3.2 | 0.097 | 17/46 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.097 | 10/48 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2999.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -6.1 | 3e-07 | 24/46 (RPMI-7951, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.650×** | -6.1 | 3e-07 | 31/48 (NCI-H661, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -5.8 | 1e-06 | 34/47 (NCI-H2347, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.693×** | -5.2 | 3e-05 | 28/48 (NCI-H2347, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.744×** | -4.2 | 0.003 | 20/48 (NCI-H2347, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.816×** | -4.1 | 0.004 | 23/48 (NCI-H661, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.742×** | -4.0 | 0.004 | 21/48 (A-427, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.594×** | -3.6 | 0.027 | 19/48 (CHP-212, NCI-H661, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.845× | -3.2 | 0.075 | 20/48 (SHP-77, CFPAC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.808× | -3.0 | 0.15 | 11/47 (H4, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2999. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 29.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 13.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -8.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -8.6) |
| [[H4 (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 20.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -9.1) |
| [[KATO III (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 28.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | — |
| [[A-172 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2999), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGDN]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[AAR2]] | +0.64 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[CCDC12]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[TTF1]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TMEM208]] | +0.62 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[DOHH]] | +0.61 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[DRG1]] | +0.60 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[METTL16]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[CWC25]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[ZNF561]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PPIE]] | +0.58 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.57 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[STT3B]] | -0.54 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[GNG12]] | -0.54 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.53 | -0.43 / -0.53 | both halves | 4e-05 |  |
| [[ADAM9]] | -0.53 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[LRP11]] | -0.53 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[WWC3]] | -0.52 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[TMEM123]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[LBR]] | -0.51 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[ARHGEF12]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[IPO5]] | -0.50 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[SPTBN1]] | -0.49 | -0.29 / -0.56 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises MRPL27's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises MRPL27's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.632). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.6, -9.0); signed map (-9.0, -13.5). **Vector** length 71.9, 14.4% of its response variance represented; |z| ≥ 3 in 677 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.9 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.8 | +5.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +1.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +3.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -4.6 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | -2.6 | +2.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.5 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L27 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,367,857-50,373,207 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bL27m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9P0M9](https://www.uniprot.org/uniprotkb/Q9P0M9) carries no function annotation.

**Summary**, from NCBI Gene [51264](https://www.ncbi.nlm.nih.gov/gene/51264):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14483) · Entrez [51264](https://www.ncbi.nlm.nih.gov/gene/51264) · UniProt [Q9P0M9](https://www.uniprot.org/uniprotkb/Q9P0M9) · Ensembl [ENSG00000108826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108826)

## Data

Gene col 2999: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2999); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2999, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2999]; `tensor/DDL_lfc|DDL_z.npy` [2999]; `embed/gene_vectors.npy` [2999]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2999 or target_col == 2999). Every well: [[MRPL27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
