---
symbol: "TWIST1"
type: "gene"
col: 4365
ensembl_id: "ENSG00000122691"
name: "twist family bHLH transcription factor 1"
location: "7p21.1"
module: 104
arm: "+"
pooled_cpm: 10.44
n_lines_expressing: 24
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 15
direction_downstream: 12
tags: ["gene", "module/104", "written"]
generated_by: "tahoemap"
---

# TWIST1

*twist family bHLH transcription factor 1* — 7p21.1

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> TWIST1 is a basic helix-loop-helix factor that patterns cranial and limb mesenchyme and, when reactivated in tumours, drives epithelial-mesenchymal transition while blunting the ARF-p53 apoptotic response.

## What it is

TWIST1 binds E-boxes as a heterodimer with E proteins such as E12/E2A, or as a homodimer; dimer choice, HLH-domain phosphorylation and competition with HAND2 set which targets it occupies, so its output follows protein-level context, not its own abundance. It patterns cranial mesenchyme; haploinsufficiency causes Saethre-Chotzen syndrome. In cancer it is the canonical EMT factor, repressing E-cadherin and required for metastasis in mouse models. A conserved C-terminal "Twist box" binds p53 and promotes its MDM2-dependent degradation; TWIST1 also lowers ARF, blunting Myc-driven apoptosis. Both routes act on protein, not transcript. Separately, Twist is a classical antagonist of myogenesis, inhibiting MyoD-family bHLH factors and MEF2-dependent transcription.

## What is uncertain

TWIST1 and [[TWIST2]] share a nearly identical bHLH domain and bind the same motif, so their regulons overlap by construction and the two near-top ranks are largely one observation. Activity read off target mRNA is doubly indirect for a factor governed by dimer partners and phosphorylation. The Twist-box/p53 mechanism was established mainly in mesenchymal and sarcoma systems, not the epithelial lines dominating this panel. TWIST1 is also broadly stress- and hypoxia-responsive, so a high rank across 379 compounds may report generic stress.

## References

- Spicer et al., 1996, Science — showed Twist inhibits myogenic bHLH factors and MEF2-dependent transcription.
- el Ghouzzi et al., 1997, Nature Genetics — TWIST mutations cause Saethre-Chotzen syndrome.
- Maestro et al., 1999, Genes & Development — Twist blocks Myc-induced apoptosis and lowers ARF, acting on the ARF/MDM2/p53 axis.
- Yang et al., 2004, Cell — Twist1 is required for metastatic dissemination in a breast cancer model.
- Piccinin et al., 2012, Cancer Cell — the Twist box binds the p53 C-terminus and promotes its MDM2-mediated degradation.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.52× (z +12.5, q 5e-33, up in 13 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HS-578T 0.158×, A-172 0.127×, NCI-H1792 0.185×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.207×, HS-578T 0.258×, HOP62 0.226×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.323×, A-427 0.205×; ⚠ cell-cycle shift, explains ~27% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (HS-578T 0.218×, hTERT-HPNE 0.197×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.191×, HS-578T 0.270×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.366×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGP]] (+0.61, fdr 1e-05), [[DCN]] (+0.58, fdr 4e-05), [[ITGA8]] (+0.57, fdr 3e-05); moves opposite to [[PSMD2]] (-0.50, fdr 4e-05), [[TUSC3]] (-0.46, fdr 5e-05), [[RAB3B]] (-0.46, fdr 1e-04).
> It is in [[Module 104]], a single-armed module (Molecules associated with elastic fibres).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 12 go from it, the strongest it → [[HAND2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4365.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.52×** | +12.5 | 5e-33 | 13/21 (A-172, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +6.3 | 9e-08 | 2/16 (SK-MEL-2, BT-474) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.2 | 9e-08 | 1/13 (J82) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.3 | 0.002 | 10/22 (SNU-423, J82, …) | rises with dose | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.3 | 0.002 | 8/21 (HOP62, A-172, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.0 | 0.006 | 6/21 (NCI-H1573, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.48×** | +3.7 | 0.015 | 4/22 (SNU-423, J82, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.015 | 4/22 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.69×** | +3.6 | 0.019 | 1/20 (LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.019 | 8/21 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.019 | 8/22 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.5 | 0.026 | 7/20 (A-427, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.28×** | +3.4 | 0.035 | 7/22 (BT-474, HOP62, …) | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4365.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (HS-578T 0.158×, A-172 0.127×, NCI-H1792 0.185×; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 3 lines (NCI-H1792 0.207×, HS-578T 0.258×, HOP62 0.226×; ⚠ cell-cycle shift, explains ~25% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 0.323×, A-427 0.205×; ⚠ cell-cycle shift, explains ~27% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (HS-578T 0.218×, hTERT-HPNE 0.197×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H1792 0.191×, HS-578T 0.270×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.366×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.478× | -3.7 | 0.12 | 11/20 (NCI-H1573, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 0.704× | -3.4 | 0.14 | 11/22 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.704× | -3.4 | 0.14 | 13/22 (NCI-H1792, HS-578T, …) | two highest doses | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.691× | -3.3 | 0.14 | 5/22 (A-427, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 52.4 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -10.5) |
| [[HS-578T (line)]] | alt | 57.3 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.218× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 67.1 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.184× (z -9.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.197× (z -9.1) |
| [[A-172 (line)]] | wt | 22.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -12.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 28.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +12.0) ⚠ position not correctable | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -9.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-427 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +9.6) | — |
| [[RPMI-7951 (line)]] | alt | 57.9 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.258× (z -8.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SNU-423 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 74.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.961 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.839 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.798 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.693 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.925 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.819 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGP]] | +0.61 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[DCN]] | +0.58 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[ITGA8]] | +0.57 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PTGFR]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[MAGI2]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 | pathway: Cell-Cell communication |
| [[IRX2]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[CCN4]] | +0.54 | +0.56 / +0.39 | both halves | 5e-05 |  |
| [[SHOX2]] | +0.52 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[C1R]] | +0.52 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[MSC-AS1]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[JAM2]] | +0.51 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SGCD]] | +0.51 | +0.49 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD2]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 | pathway: Adherens junctions interactions |
| [[TUSC3]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[RAB3B]] | -0.46 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[PXN]] | -0.46 | -0.37 / -0.48 | both halves | 8e-05 | pathway: Cell junction organization |
| [[CORO2B]] | -0.45 | -0.43 / -0.47 | both halves | 4e-05 |  |
| [[TRMT2B]] | -0.43 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[RGS4]] | -0.43 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[NRIP3]] | -0.43 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[ZNF731P]] | -0.42 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[ZDHHC21]] | -0.42 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[TOMM34]] | -0.42 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[CHCHD6]] | -0.42 | -0.41 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 1, C 14. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TWIST1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GYPC]] | C | GYPC activity raises TWIST1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 7.25× lower at baseline in the lines without GYPC | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4; co-absent with the target |
| [[FAP]] | C | FAP activity raises TWIST1's level | lines that do not express FAP (25) vs lines expressing it (25) | 6.53× lower at baseline in the lines without FAP | 0.011 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, PTPRD, KCNQ5; co-absent with the target |
| [[LINC00882]] | C | LINC00882 activity raises TWIST1's level | lines that do not express LINC00882 (17) vs lines expressing it (33) | 5.10× lower at baseline in the lines without LINC00882 | 0.014 | ⚠ within organs, on part of the lines; also absent: TUSC3, B3GALT1, EVC; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises TWIST1's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 5.25× lower at baseline in the lines without LINC01687 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |
| [[NNMT]] | C | NNMT activity raises TWIST1's level | lines that do not express NNMT (24) vs lines expressing it (26) | 3.69× lower at baseline in the lines without NNMT | 0.031 | ⚠ within organs, on part of the lines; also absent: KC6, DPYSL3, ENSG00000230615; co-absent with the target |
| [[PRR16]] | C | PRR16 activity raises TWIST1's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 6.17× lower at baseline in the lines without PRR16 | 0.051 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[ZIC1]] | C | ZIC1 activity raises TWIST1's level | lines that do not express ZIC1 (34) vs lines expressing it (16) | 5.94× lower at baseline in the lines without ZIC1 | 0.056 | ⚠ within organs, on part of the lines; also absent: PCDH18, MDGA2, DCN; co-absent with the target |
| [[KC6]] | C | KC6 activity raises TWIST1's level | lines that do not express KC6 (32) vs lines expressing it (18) | 6.18× lower at baseline in the lines without KC6 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[MAGI2-AS3]] | C | MAGI2-AS3 activity raises TWIST1's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 4.98× lower at baseline in the lines without MAGI2-AS3 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises TWIST1's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 3.86× lower at baseline in the lines without ADAMTS2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[MSC-AS1]] | C | MSC-AS1 activity raises TWIST1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 5.78× lower at baseline in the lines without MSC-AS1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAND2-AS1]] | B | TWIST1 activity raises HAND2-AS1's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without TWIST1 | 0.028 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP |
| [[LINC01687]] | C | TWIST1 activity raises LINC01687's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 4.30× lower at baseline in the lines without TWIST1 | 0.009 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[PRR16]] | C | TWIST1 activity raises PRR16's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 9.73× lower at baseline in the lines without TWIST1 | 0.011 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[GYPC]] | C | TWIST1 activity raises GYPC's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 3.84× lower at baseline in the lines without TWIST1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[ADAMTS2]] | C | TWIST1 activity raises ADAMTS2's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 2.77× lower at baseline in the lines without TWIST1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[LINC00882]] | C | TWIST1 activity raises LINC00882's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 3.88× lower at baseline in the lines without TWIST1 | 0.025 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[JAM2]] | C | TWIST1 activity raises JAM2's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 2.85× lower at baseline in the lines without TWIST1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[PDGFRA]] | C | TWIST1 activity raises PDGFRA's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 2.32× lower at baseline in the lines without TWIST1 | 0.038 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[MSC-AS1]] | C | TWIST1 activity raises MSC-AS1's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 7.03× lower at baseline in the lines without TWIST1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[ZIC1]] | C | TWIST1 activity raises ZIC1's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 3.57× lower at baseline in the lines without TWIST1 | 0.046 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[TMEM45A]] | C | TWIST1 activity raises TMEM45A's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 3.90× lower at baseline in the lines without TWIST1 | 0.049 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |
| [[ITGA8]] | C | TWIST1 activity raises ITGA8's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without TWIST1 | 0.097 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP; co-absent with the target |

## Where it sits

- **Module**: [[Module 104]] — Molecules associated with elastic fibres; 44 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.5, 23.0); signed map (24.1, 38.3). **Vector** length 69.5, 20.0% of its response variance represented; |z| ≥ 3 in 556 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +12.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +4.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.3 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.9 | +2.6 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.8 | -2.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.7 | -2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | twist family bHLH transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:19,020,991-19,117,636 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCS, H-twist, BPES2, bHLHa38, CRS1; previously ACS3, BPES3, TWIST, CRS |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Reactome | 18 pathways, smallest: Nuclear events stimulated by ALK signaling in cancer; Negative Regulation of CDH1 Gene Transcription; Regulation of RUNX2 expression and activity |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15672](https://www.uniprot.org/uniprotkb/Q15672) (Twist-related protein 1):

> Acts as a transcriptional regulator. Inhibits myogenesis by sequestrating E proteins, inhibiting trans-activation by MEF2, and inhibiting DNA-binding by MYOD1 through physical interaction. This interaction probably involves the basic domains of both proteins. Also represses expression of pro-inflammatory cytokines such as TNFA and IL1B. Regulates cranial suture patterning and fusion. Activates transcription as a heterodimer with E proteins. Regulates gene expression differentially, depending on …

**Summary**, from NCBI Gene [7291](https://www.ncbi.nlm.nih.gov/gene/7291):

> This gene encodes a basic helix-loop-helix (bHLH) transcription factor that plays an important role in embryonic development. The encoded protein forms both homodimers and heterodimers that bind to DNA E box sequences and regulate the transcription of genes involved in cranial suture closure during skull development. This protein may also regulate neural tube closure, limb development and brown fat metabolism. This gene is hypermethylated and overexpressed in multiple human cancers, and the …

**Accessions** — [HGNC:12428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12428) · Entrez [7291](https://www.ncbi.nlm.nih.gov/gene/7291) · UniProt [Q15672](https://www.uniprot.org/uniprotkb/Q15672) · Ensembl [ENSG00000122691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122691)

## Data

Gene col 4365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4365); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4365]; `tensor/DDL_lfc|DDL_z.npy` [4365]; `embed/gene_vectors.npy` [4365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4365 or target_col == 4365). Every well: [[TWIST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/TWIST1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
