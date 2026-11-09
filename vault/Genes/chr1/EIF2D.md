---
symbol: "EIF2D"
type: "gene"
col: 6754
ensembl_id: "ENSG00000143486"
name: "eukaryotic translation initiation factor 2D"
location: "1q32.1"
module: 20
arm: "+"
pooled_cpm: 19.92
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EIF2D

*eukaryotic translation initiation factor 2D* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.87× (z +11.6, q 2e-28, up in 24 of 32 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.37× (z +8.7, q 5e-16, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.729× (z -6.1, q 5e-07, down in 22 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0561×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.137×; ⚠ cell-cycle shift, would explain all of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (Hs 766T 0.115×; ⚠ toxic); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.448×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NNT]] (+0.67, fdr 3e-05), [[NCSTN]] (+0.66, fdr 7e-06), [[MED24]] (+0.65, fdr 1e-05); moves opposite to [[MIDN]] (-0.66, fdr 2e-05), [[PLIN3]] (-0.64, fdr 4e-05), [[LUZP1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +11.6 | 2e-28 | 24/32 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +9.3 | 4e-18 | 31/41 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +8.7 | 5e-16 | 31/48 (A-427, CFPAC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +7.3 | 3e-11 | 23/48 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +6.2 | 8e-08 | 24/48 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +5.9 | 3e-07 | 18/35 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +4.6 | 4e-04 | 17/47 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.20×** | +3.6 | 0.027 | 17/45 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.19× | +3.4 | 0.039 | 12/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | 1.36× | +3.1 | 0.11 | 4/47 (HCT15, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.18× | +3.0 | 0.13 | 11/47 (A-427, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6754.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0561×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.137×; ⚠ cell-cycle shift, would explain all of this change); [[AZD2858 (drug)]] 0.5 µM in 1 line (Hs 766T 0.115×; ⚠ toxic); [[Belinostat (drug)]] 5 µM in 1 line (NCI-H460 0.448×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.729×** | -6.1 | 5e-07 | 22/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.773×** | -5.0 | 2e-04 | 20/48 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -4.6 | 0.001 | 14/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.805×** | -4.2 | 0.004 | 15/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 0.5 µM |  | 0.838× | -3.4 | 0.074 | 9/46 (NCI-H661, CFPAC-1, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.846× | -3.2 | 0.12 | 15/46 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 0.731× | -3.2 | 0.12 | 11/46 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.891× | -3.1 | 0.12 | 9/48 (SW 1271, LoVo, …) | top dose only |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.855× | -3.0 | 0.16 | 10/46 (H4, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0561× (z -14.0) |
| [[Hs 766T (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.115× (z -11.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.01× (z +12.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 28.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.448× (z -8.8) |
| [[PANC-1 (line)]] | alt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.75× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 35.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 22.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NNT]] | +0.67 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[NCSTN]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[MED24]] | +0.65 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[EEF1A1P5]] | +0.65 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[EEF1A1]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CERS2]] | +0.62 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[NAXD]] | +0.62 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[RAB11FIP2]] | +0.61 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[ZCCHC4]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[UNC119B]] | +0.61 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[UHMK1]] | +0.60 | +0.37 / +0.59 | both halves | 8e-05 |  |
| [[CIPC]] | +0.60 | +0.43 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIDN]] | -0.66 | -0.48 / -0.71 | both halves | 2e-05 |  |
| [[PLIN3]] | -0.64 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[LUZP1]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.61 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[POLD4]] | -0.57 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ZBTB7A]] | -0.56 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[TMEM191A-1]] | -0.55 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[ZSWIM6]] | -0.55 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[EHD4]] | -0.54 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[ARID3B]] | -0.53 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[DUSP5]] | -0.53 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[KLF2]] | -0.53 | -0.38 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises EIF2D's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.503). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-11.0, 8.5); signed map (-18.8, -32.4). **Vector** length 73.9, 12.5% of its response variance represented; |z| ≥ 3 in 803 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +5.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.6 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.6 | +2.8 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -3.2 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.1 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.5 | -6.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -0.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.5 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:206,571,292-206,612,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LGTN |
| Matched by | ensembl_id |

**Function**, from UniProt [P41214](https://www.uniprot.org/uniprotkb/P41214) (Eukaryotic translation initiation factor 2D):

> Translation initiation factor that is able to deliver tRNA to the P-site of the eukaryotic ribosome in a GTP-independent manner. The binding of Met-tRNA(I) occurs after the AUG codon finds its position in the P-site of 40S ribosomes, the situation that takes place during initiation complex formation on some specific RNAs. Its activity in tRNA binding with 40S subunits does not require the presence of the aminoacyl moiety. Possesses the unique ability to deliver non-Met (elongator) tRNAs into …

**Summary**, from NCBI Gene [1939](https://www.ncbi.nlm.nih.gov/gene/1939):

> This gene encodes a translation initiation factor involved in the recruitment and delivery of aminoacyl-tRNAs to the P-site of the eukaryotic ribosome in a GTP-independent manner. This gene was previously referred to as ligatin, but is now known to localize to the cytoplasm and localize and function with translation factors. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jan 2011]

**Accessions** — [HGNC:6583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6583) · Entrez [1939](https://www.ncbi.nlm.nih.gov/gene/1939) · UniProt [P41214](https://www.uniprot.org/uniprotkb/P41214) · Ensembl [ENSG00000143486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143486)

## Data

Gene col 6754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6754); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6754]; `tensor/DDL_lfc|DDL_z.npy` [6754]; `embed/gene_vectors.npy` [6754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6754 or target_col == 6754). Every well: [[EIF2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
