---
symbol: "TCTN2"
type: "gene"
col: 9696
ensembl_id: "ENSG00000168778"
name: "tectonic family member 2"
location: "12q24.31"
module: 205
arm: "+"
pooled_cpm: 12.2
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# TCTN2

*tectonic family member 2* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.51× (z +9.9, q 1e-20, up in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.62× (z +8.2, q 7e-14, up in 27 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.592× (z -12.7, q 4e-34, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A14]] (+0.63, fdr 3e-05), [[TMEM234]] (+0.63, fdr 1e-05), [[MED25]] (+0.62, fdr 1e-05); moves opposite to [[EIF4G3]] (-0.54, fdr 3e-05), [[NPL]] (-0.53, fdr 1e-04), [[DDX21]] (-0.53, fdr 3e-05).
> It is in [[Module 205]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TMUB2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.51×** | +9.9 | 1e-20 | 30/47 (LoVo, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +8.2 | 7e-14 | 27/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +7.6 | 8e-12 | 25/47 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.43×** | +6.1 | 2e-07 | 21/47 (LoVo, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +5.9 | 4e-07 | 20/46 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +5.9 | 4e-07 | 22/47 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +5.2 | 2e-05 | 12/47 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +4.4 | 7e-04 | 16/46 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.3 | 0.001 | 12/47 (LoVo, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.0 | 0.003 | 19/44 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +4.0 | 0.003 | 6/46 (KATO III, HT-29, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.004 | 5/41 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.6 | 0.012 | 4/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.019 | 10/47 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.079 | 7/47 (KATO III, J82, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.20×** | +3.0 | 0.097 | 10/46 (SNU-423, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.0 | 0.097 | 7/46 (KATO III, NCI-H661, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.592×** | -12.7 | 4e-34 | 39/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.490×** | -12.2 | 6e-32 | 36/46 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.594×** | -8.9 | 9e-17 | 27/46 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.753×** | -4.9 | 1e-04 | 18/44 (A-172, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -4.8 | 1e-04 | 21/38 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **0.631×** | -4.1 | 0.003 | 14/43 (J82, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.785×** | -4.0 | 0.005 | 11/46 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.799×** | -3.9 | 0.007 | 11/46 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.792×** | -3.9 | 0.007 | 16/46 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Thymol (drug)]] 5 µM |  | 0.868× | -3.5 | 0.029 | 16/47 (H4, SW 1088, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.818×** | -3.4 | 0.029 | 15/47 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.816×** | -3.4 | 0.037 | 8/46 (SNU-1, RPMI-7951, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.829×** | -3.2 | 0.051 | 18/46 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.05 µM |  | **0.820×** | -3.2 | 0.051 | 8/45 (A549, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 19.3 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.184× (z -12.2) |
| [[Hs 766T (line)]] | wt | 7.15 | 0 | 3 (1 ⚠) | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0881× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 3 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.156× (z -14.5) |
| [[CFPAC-1 (line)]] | alt | 21.7 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 5 µM 0.393× (z -10.2) |
| [[LoVo (line)]] | wt | 9.41 | 1 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.75× (z +8.7) ⚠ cell-cycle shift, explains ~25% of this change | [[AZD2858 (drug)]] 0.5 µM 0.0934× (z -10.3) ⚠ toxic |
| [[C32 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 11.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0769× (z -8.9) |
| [[HOP62 (line)]] | alt | 17.8 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.351× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.217× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 7.54 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 1 | — | [[Tucidinostat (drug)]] 0.5 µM 0.298× (z -9.0) |
| [[PANC-1 (line)]] | alt | 11.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.21× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0641× (z -20.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.26 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A14]] | +0.63 | +0.46 / +0.75 | both halves | 3e-05 |  |
| [[TMEM234]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MED25]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CDC23]] | +0.59 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[CEP43]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 | pathway: Anchoring of the basal body to the plasma membrane |
| [[ATF6B]] | +0.58 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[DNAL1]] | +0.58 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DZANK1]] | +0.58 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[FAM174A]] | +0.58 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[LMAN2L]] | +0.57 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[VPS11]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[BBS1]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 506 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G3]] | -0.54 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[NPL]] | -0.53 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[DDX21]] | -0.53 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[TJP1]] | -0.47 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[MEGF11]] | -0.47 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[CDH4]] | -0.47 | -0.56 / -0.43 | both halves | 4e-05 |  |
| [[DUSP5]] | -0.47 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[KLHL29]] | -0.46 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[ERC2]] | -0.45 | -0.26 / -0.56 | both halves | 4e-04 |  |
| [[MAMLD1]] | -0.45 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[PLAAT1]] | -0.45 | -0.29 / -0.54 | both halves | 2e-04 |  |
| [[CDV3]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMUB2]] | C | TCTN2's natural level strengthens TMUB2's drug response | TCTN2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.25; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.626). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.8, 21.7); signed map (-20.0, 5.4). **Vector** length 88.9, 17.3% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +7.0 | +9.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.8 | +6.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.7 | +5.9 |
|  | [[NG25 (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.6 | +4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +0.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.3 | +2.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -10.7 | -12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -8.1 | -12.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -8.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -4.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -3.3 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -3.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | tectonic family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,671,110-123,708,399 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12975, TECT2, MKS8, JBTS24; previously C12orf38 |
| Gene groups (HGNC) | Tectonic proteins; MKS complex |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GX1](https://www.uniprot.org/uniprotkb/Q96GX1) (Tectonic-2):

> Component of the tectonic-like complex, a complex localized at the transition zone of primary cilia and acting as a barrier that prevents diffusion of transmembrane proteins between the cilia and plasma membranes. Required for hedgehog signaling transduction (By similarity).

**Summary**, from NCBI Gene [79867](https://www.ncbi.nlm.nih.gov/gene/79867):

> This gene encodes a type I membrane protein that belongs to the tectonic family. Studies in mice suggest that this protein may be involved in hedgehog signaling, and essential for ciliogenesis. Mutations in this gene are associated with Meckel syndrome type 8. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:25774](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25774) · Entrez [79867](https://www.ncbi.nlm.nih.gov/gene/79867) · UniProt [Q96GX1](https://www.uniprot.org/uniprotkb/Q96GX1) · Ensembl [ENSG00000168778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168778)

## Data

Gene col 9696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9696); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9696]; `tensor/DDL_lfc|DDL_z.npy` [9696]; `embed/gene_vectors.npy` [9696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9696 or target_col == 9696). Every well: [[TCTN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCTN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
