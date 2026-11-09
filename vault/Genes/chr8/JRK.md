---
symbol: "JRK"
type: "gene"
col: 13970
ensembl_id: "ENSG00000234616"
name: "Jrk helix-turn-helix protein"
location: "8q24.3"
module: 36
arm: "+"
pooled_cpm: 9.92
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 15
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# JRK

*Jrk helix-turn-helix protein* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.61× (z +6.9, q 3e-09, up in 20 of 39 measured lines) ⚠ toxic. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.43× (z +5.7, q 3e-06, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.414× (z -19.6, q 0e+00, down in 39 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPUSD4]] (+0.59, fdr 1e-05), [[SFXN4]] (+0.59, fdr 1e-05), [[MAFIP]] (+0.59, fdr 2e-05); moves opposite to [[SKAP2]] (-0.50, fdr 2e-05), [[SHOC2]] (-0.50, fdr 1e-05), [[PPM1K]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13970.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +6.9 | 3e-09 | 20/39 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.7 | 3e-06 | 22/46 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.18× | +3.7 | 0.026 | 12/48 (A549, A498, …) | rises with dose | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.026 | 6/42 (NCI-H1792, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.23× | +3.3 | 0.11 | 10/46 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.23× | +3.2 | 0.11 | 4/48 (LoVo, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13970.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.414×** | -19.6 | 0e+00 | 39/46 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.409×** | -12.9 | 2e-35 | 33/46 (C32, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.467×** | -11.1 | 2e-26 | 33/43 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -9.2 | 8e-18 | 26/44 (PANC-1, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.591×** | -8.3 | 2e-14 | 27/46 (C32, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.594×** | -8.2 | 2e-14 | 25/47 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.636×** | -7.1 | 1e-10 | 23/47 (C-33 A, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.709×** | -5.4 | 5e-06 | 17/47 (A-427, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -5.3 | 8e-06 | 17/38 (SHP-77, COLO 205, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.741×** | -4.7 | 1e-04 | 16/47 (Hs 766T, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -4.4 | 5e-04 | 17/45 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.771×** | -4.1 | 0.002 | 12/47 (NCI-H1792, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.787×** | -3.4 | 0.026 | 12/45 (RKO, C-33 A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.814×** | -3.2 | 0.052 | 9/43 (hTERT-HPNE, SK-MEL-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.822×** | -3.1 | 0.083 | 10/47 (AN3 CA, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13970. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 11.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 7.06 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0780× (z -19.4) |
| [[SW480 (line)]] | alt | 10.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.9) |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -15.4) |
| [[A-427 (line)]] | wt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.5) |
| [[A549 (line)]] | wt | 8.36 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 8.30 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -8.7) |
| [[BT-474 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 6.10 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.0) |
| [[H4 (line)]] | wt | 11.4 | 0 | 1 | — | [[EX229 (drug)]] 0.05 µM 0.0652× (z -9.0) |
| [[Hs 766T (line)]] | wt | 11.7 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.137× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 7.34 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 9.53 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0384× (z -13.1) |
| [[RKO (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -8.7) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SHP-77 (line)]] | alt | 8.21 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0970× (z -8.8) |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0973× (z -8.8) |
| [[SW 900 (line)]] | alt | 5.70 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0506× (z -10.1) |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.7) |
| [[SW48 (line)]] | wt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0741× (z -8.6) |
| [[A-172 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13970), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPUSD4]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[SFXN4]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[MAFIP]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[SPHK2]] | +0.58 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[DDX54]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[GTF3C2]] | +0.57 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[MED9]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[NAGPA]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ZNF12]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[CTU1]] | +0.56 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[OGFOD3]] | +0.55 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[ZNF551]] | +0.55 | +0.48 / +0.58 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKAP2]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SHOC2]] | -0.50 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PPM1K]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[SUB1]] | -0.49 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[MED29]] | -0.48 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[GOLGB1]] | -0.48 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[EEA1]] | -0.48 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[UACA]] | -0.48 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[MPC1]] | -0.47 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[NUMB]] | -0.45 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[RO60]] | -0.44 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[CDKL5]] | -0.44 | -0.46 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises JRK's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.451). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-29.6, -7.3); signed map (-15.2, -19.7). **Vector** length 67.7, 10.4% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | +3.6 | +3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[EX229 (drug)]] 5 µM |  | +1.7 | +1.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.6 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -12.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -19.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.1 | -11.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -2.5 | -3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | Jrk helix-turn-helix protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:142,657,460-142,681,968 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JH8, jerky |
| Gene groups (HGNC) | Helix-turn-helix CENPB type domain family |
| Matched by | ensembl_id |

**Function**, from UniProt [O75564](https://www.uniprot.org/uniprotkb/O75564) (Jerky protein homolog):

> May bind DNA.

**Summary**, from NCBI Gene [8629](https://www.ncbi.nlm.nih.gov/gene/8629):

> This gene encodes a conserved protein that is similar to DNA-binding proteins, such as major centromere autoantigen B (CENPB). Inactivation of the related gene in mice resulted in epileptic seizures. Childhood Absence Epilepsy (CAE) has been mapped to the same chromosomal location (8q24.3) as this gene. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2013]

**Accessions** — [HGNC:6199](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6199) · Entrez [8629](https://www.ncbi.nlm.nih.gov/gene/8629) · UniProt [O75564](https://www.uniprot.org/uniprotkb/O75564) · Ensembl [ENSG00000234616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234616)

## Data

Gene col 13970: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13970); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13970, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13970]; `tensor/DDL_lfc|DDL_z.npy` [13970]; `embed/gene_vectors.npy` [13970]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13970 or target_col == 13970). Every well: [[JRK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JRK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
