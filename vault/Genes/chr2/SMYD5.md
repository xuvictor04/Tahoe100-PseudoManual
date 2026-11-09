---
symbol: "SMYD5"
type: "gene"
col: 5734
ensembl_id: "ENSG00000135632"
name: "SMYD family member 5"
location: "2p13.2"
module: 1
arm: "+"
pooled_cpm: 11.99
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# SMYD5

*SMYD family member 5* — 2p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.49× (z +5.6, q 9e-06, up in 24 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.49× (z +5.5, q 9e-06, up in 21 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.439× (z -11.5, q 1e-27, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZPR1]] (+0.76, fdr 7e-06), [[ZNF202]] (+0.68, fdr 1e-05), [[QTRT1]] (+0.67, fdr 1e-05); moves opposite to [[RNF24]] (-0.57, fdr 3e-05), [[PCSK1N]] (-0.56, fdr 9e-05), [[CYP46A1]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +5.6 | 9e-06 | 24/47 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +5.5 | 9e-06 | 21/46 (NCI-H2030, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 1e-04 | 19/47 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.5 | 0.001 | 18/48 (LoVo, A-427, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.004 | 19/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.036 | 18/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +3.2 | 0.094 | 10/45 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.094 | 8/44 (SHP-77, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.17× | +3.1 | 0.11 | 13/48 (NCI-H1573, NCI-H2347, …) | rises with dose | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5734.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.439×** | -11.5 | 1e-27 | 36/47 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.446×** | -11.2 | 8e-27 | 35/48 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.486×** | -10.0 | 2e-21 | 35/48 (NCI-H23, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.541×** | -8.5 | 2e-15 | 34/48 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.728×** | -6.2 | 6e-08 | 26/48 (A498, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.644×** | -6.1 | 9e-08 | 24/43 (A-172, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -5.6 | 2e-06 | 25/46 (A-427, C32, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.509×** | -4.9 | 7e-05 | 21/43 (SW480, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.555×** | -4.3 | 0.001 | 13/48 (A498, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.735×** | -4.3 | 0.001 | 22/46 (SK-MEL-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -4.0 | 0.003 | 15/46 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.787×** | -3.3 | 0.043 | 12/44 (SW48, SNU-1, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.795×** | -3.2 | 0.066 | 13/47 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.1 | 0.070 | 6/48 (MIA PaCa-2, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.249× (z -9.7) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 2 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0644× (z -15.9) |
| [[A-427 (line)]] | wt | 20.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.148× (z -10.0) ⚠ toxic |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 1 | — | [[Bestatin (drug)]] 0.05 µM 0.101× (z -8.5) |
| [[HOP62 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.265× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 7.95 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.132× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 7.50 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0775× (z -9.0) |
| [[J82 (line)]] | alt | 7.34 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.133× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.163× (z -9.7) |
| [[RKO (line)]] | wt | 12.7 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -10.2) |
| [[SW48 (line)]] | wt | 11.6 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0579× (z -10.1) |
| [[A498 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZPR1]] | +0.76 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[ZNF202]] | +0.68 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[QTRT1]] | +0.67 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PRMT5]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[FASTKD2]] | +0.65 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[METTL1]] | +0.64 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[KICS2]] | +0.63 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[RBM28]] | +0.63 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ZNF783]] ⚠ | +0.63 | +0.56 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DIMT1]] | +0.63 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[DUS3L]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PUM3]] | +0.61 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TTC27]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF24]] | -0.57 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[PCSK1N]] | -0.56 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[CYP46A1]] | -0.55 | -0.39 / -0.47 | both halves | 6e-05 |  |
| [[CARHSP1]] | -0.54 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[COX6A1]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[DNAJC1]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers SMYD5's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SMARCAL1]] | C | SMARCAL1's natural level strengthens SMYD5's drug response | SMARCAL1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.17; direction not clear | 0.076 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.5, -35.0); signed map (-2.0, -43.6). **Vector** length 71.0, 11.5% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.50 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.2 | +5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.1 | +1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -6.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.3 | -11.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -1.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -4.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SMYD family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.2 — chr2:73,214,222-73,227,221 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RRG1, NN8-4AG, ZMYND23; previously RAI15 |
| Gene groups (HGNC) | Zinc fingers MYND-type; SET domain containing; Non-histone lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6GMV2](https://www.uniprot.org/uniprotkb/Q6GMV2) (Protein-lysine N-trimethyltransferase SMYD5):

> Protein-lysine N-trimethyltransferase that specifically catalyzes trimethylation of 'Lys-22' of the RPL40/eL40 subunit of the 60S ribosome, thereby promoting translation elongation and protein synthesis. May also act as a histone methyltransferase in the context of histone octamers, but not on nucleosome substrates: trimethylates 'Lys-36' of histone H3 and 'Lys-20' of histone H4 to form H3K36me3 and H4K20me3, respectively (By similarity). The histone methyltransferase activity, which is …

**Summary**, from NCBI Gene [10322](https://www.ncbi.nlm.nih.gov/gene/10322):

> Enables protein-lysine N-methyltransferase activity. Involved in positive regulation of cytoplasmic translational elongation; regulation of stem cell differentiation; and transposable element silencing by heterochromatin formation. Is active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16258) · Entrez [10322](https://www.ncbi.nlm.nih.gov/gene/10322) · UniProt [Q6GMV2](https://www.uniprot.org/uniprotkb/Q6GMV2) · Ensembl [ENSG00000135632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135632)

## Data

Gene col 5734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5734); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5734]; `tensor/DDL_lfc|DDL_z.npy` [5734]; `embed/gene_vectors.npy` [5734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5734 or target_col == 5734). Every well: [[SMYD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMYD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
