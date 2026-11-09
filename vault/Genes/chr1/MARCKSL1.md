---
symbol: "MARCKSL1"
type: "gene"
col: 10566
ensembl_id: "ENSG00000175130"
name: "MARCKS like 1"
location: "1p35.1"
module: 12
arm: "-"
pooled_cpm: 27.79
n_lines_expressing: 48
n_dd_up: 16
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# MARCKSL1

*MARCKS like 1* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.87× (z +13.2, q 9e-37, up in 39 of 42 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +6.5, q 6e-09, up in 34 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.675× (z -4.7, q 0.001, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VMA21]] (+0.53, fdr 2e-05), [[CELSR2]] (+0.53, fdr 5e-05), [[SIGMAR1]] (+0.53, fdr 3e-05); moves opposite to [[DNAJC2]] (-0.58, fdr 1e-05), [[PPIG]] (-0.56, fdr 1e-05), [[GPATCH1]] (-0.53, fdr 2e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.87×** | +13.2 | 9e-37 | 39/42 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **2.60×** | +11.4 | 8e-28 | 28/35 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.32×** | +9.7 | 6e-20 | 31/39 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +9.2 | 7e-18 | 36/42 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.93×** | +8.2 | 3e-14 | 32/46 (J82, HOP62, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.79×** | +7.3 | 3e-11 | 33/46 (J82, HOP62, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +6.8 | 8e-10 | 37/44 (HOP62, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +6.5 | 6e-09 | 34/46 (J82, PANC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +6.0 | 2e-07 | 23/46 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.50×** | +5.1 | 2e-05 | 24/45 (HOP62, J82, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.31×** | +4.7 | 1e-04 | 19/44 (A549, J82, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.46×** | +4.5 | 3e-04 | 21/43 (A-427, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +4.5 | 3e-04 | 19/45 (J82, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.001 | 23/46 (HepG2/C3A, J82, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.37×** | +3.7 | 0.007 | 16/44 (HOP62, J82, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.035 | 14/46 (A-427, NCI-H23, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.675×** | -4.7 | 0.001 | 25/45 (COLO 205, HT-29, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.697×** | -4.5 | 0.001 | 22/45 (COLO 205, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.698×** | -4.5 | 0.001 | 25/45 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.718×** | -4.1 | 0.005 | 19/46 (LS 180, KATO III, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.825×** | -3.4 | 0.070 | 13/46 (SW480, SHP-77, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.605×** | -3.3 | 0.096 | 18/46 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.772×** | -3.2 | 0.098 | 15/45 (KATO III, HT-29, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.766× | -3.2 | 0.11 | 17/45 (LOX-IMVI, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HOP62 (line)]] | alt | 22.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.09× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[J82 (line)]] | alt | 31.4 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[KATO III (line)]] | alt | 53.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -9.4) |
| [[RKO (line)]] | wt | 49.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -10.0) |
| [[C-33 A (line)]] | alt | 66.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -13.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -11.6) |
| [[C32 (line)]] | wt | 19.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.56× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[LS 180 (line)]] | wt | 65.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Harringtonine (drug)]] 5 µM 0.305× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 62.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -11.9) |
| [[COLO 205 (line)]] | alt | 45.9 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.138× (z -10.9) |
| [[HT-29 (line)]] | alt | 61.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.311× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 48.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.46× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 8.93 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.89× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[A-172 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.77 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CELSR2]] | +0.53 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[SIGMAR1]] | +0.53 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[ACTB]] | +0.52 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[TAGLN2]] | +0.52 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[FLNA]] | +0.52 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[CMTM6]] | +0.51 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[PKM]] | +0.51 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[CD164]] | +0.51 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[MOB1A]] | +0.51 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[DAG1]] | +0.51 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[BSG]] | +0.50 | +0.57 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | -0.58 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[PPIG]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[GPATCH1]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[DHX29]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ZNF500]] | -0.52 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[ZSWIM9]] | -0.52 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[LRSAM1]] | -0.51 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[RBMX2]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[EXOSC1]] | -0.51 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[BMS1P4-1]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[MRPL23]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SLC4A1AP]] | -0.50 | -0.50 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises MARCKSL1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers MARCKSL1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.460). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-46.3, -3.9); signed map (-6.0, 33.8). **Vector** length 109, 28.6% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.9 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.1 | +9.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.1 | +1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +1.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.8 | +3.3 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | +1.6 | +1.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.3 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -4.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.0 | -2.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.4 | -1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | MARCKS like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,333,839-32,336,233 (-) |
| Ensembl biotype | protein_coding |
| Also known as | F52, MacMARCKS, MLP1; previously MLP |
| Matched by | ensembl_id |

**Function**, from UniProt [P49006](https://www.uniprot.org/uniprotkb/P49006) (MARCKS-related protein):

> Controls cell movement by regulating actin cytoskeleton homeostasis and filopodium and lamellipodium formation. When unphosphorylated, induces cell migration (By similarity). When phosphorylated by MAPK8, induces actin bundles formation and stabilization, thereby reducing actin plasticity, hence restricting cell movement, including neuronal migration (By similarity). May be involved in coupling the protein kinase C and calmodulin signal transduction systems (By similarity).

**Summary**, from NCBI Gene [65108](https://www.ncbi.nlm.nih.gov/gene/65108):

> This gene encodes a member of the myristoylated alanine-rich C-kinase substrate (MARCKS) family. Members of this family play a role in cytoskeletal regulation, protein kinase C signaling and calmodulin signaling. The encoded protein affects the formation of adherens junction. Alternative splicing results in multiple transcript variants. Pseudogenes of this gene are located on the long arm of chromosomes 6 and 10. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:7142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7142) · Entrez [65108](https://www.ncbi.nlm.nih.gov/gene/65108) · UniProt [P49006](https://www.uniprot.org/uniprotkb/P49006) · Ensembl [ENSG00000175130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175130)

## Data

Gene col 10566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10566); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10566]; `tensor/DDL_lfc|DDL_z.npy` [10566]; `embed/gene_vectors.npy` [10566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10566 or target_col == 10566). Every well: [[MARCKSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MARCKSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
