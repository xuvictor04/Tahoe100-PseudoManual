---
symbol: "SEC61A1"
type: "gene"
col: 658
ensembl_id: "ENSG00000058262"
name: "SEC61 translocon subunit alpha 1"
location: "3q21.3"
module: 42
arm: "+"
pooled_cpm: 141.08
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# SEC61A1

*SEC61 translocon subunit alpha 1* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.64× (z +7.4, q 8e-11, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.377× (z -18.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF4]] (+0.84, fdr 7e-06), [[COPG1]] (+0.82, fdr 7e-06), [[TMEM39A]] (+0.81, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GALNT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 658.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +7.4 | 8e-11 | 43/48 (Panc 03.27, SHP-77, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +5.7 | 3e-06 | 42/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.006 | 39/48 (SW480, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.056 | 29/48 (NCI-H1792, C32, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.065 | 27/48 (NCI-H1792, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 658.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.377×** | -18.7 | 0e+00 | 46/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.406×** | -13.0 | 5e-36 | 46/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -8.9 | 9e-17 | 35/48 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.622×** | -7.1 | 2e-10 | 39/48 (A-172, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.655×** | -6.3 | 3e-08 | 36/48 (SW 1088, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -4.6 | 3e-04 | 33/48 (HS-578T, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.746×** | -4.2 | 0.002 | 29/48 (J82, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.740×** | -4.2 | 0.002 | 28/47 (A549, LoVo, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.774×** | -3.8 | 0.008 | 34/48 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.786×** | -3.6 | 0.018 | 28/49 (H4, C32, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.833× | -3.4 | 0.035 | 24/49 (J82, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.3 | 0.044 | 20/48 (HS-578T, hTERT-HPNE, …) | top dose only | low cells (technical?) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.803×** | -3.3 | 0.044 | 24/49 (MIA PaCa-2, KATO III, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.807×** | -3.2 | 0.052 | 23/48 (RPMI-7951, HT-29, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.815×** | -3.1 | 0.082 | 24/48 (HS-578T, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 658. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 366 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -30.2) |
| [[A-172 (line)]] | wt | 133 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -20.7) |
| [[J82 (line)]] | alt | 432 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -23.6) |
| [[NCI-H2347 (line)]] | alt | 155 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -24.0) |
| [[A-427 (line)]] | wt | 107 | 0 | 4 | — | [[Harringtonine (drug)]] 0.5 µM 0.375× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 206 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.7) |
| [[PANC-1 (line)]] | alt | 91.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -15.7) |
| [[A498 (line)]] | wt | 200 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -16.5) |
| [[A549 (line)]] | wt | 76.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -16.3) |
| [[RPMI-7951 (line)]] | alt | 224 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -18.0) |
| [[SW 900 (line)]] | alt | 137 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -13.2) |
| [[C-33 A (line)]] | alt | 58.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -9.3) |
| [[LoVo (line)]] | wt | 148 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.276× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 75.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 105 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 94.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 103 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.1) |
| [[SNU-1 (line)]] | wt | 116 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -12.2) |
| [[SW 1271 (line)]] | alt | 83.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -11.7) |
| [[SW480 (line)]] | alt | 114 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.1) |
| [[AsPC-1 (line)]] | alt | 109 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -8.7) |
| [[BT-474 (line)]] | alt | 91.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 120 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -13.1) |
| [[H4 (line)]] | wt | 246 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.8) |
| [[HCT15 (line)]] | alt | 181 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.250× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -10.5) |
| [[HOP62 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.1) |
| [[Hs 766T (line)]] | wt | 123 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -9.4) |
| [[HT-29 (line)]] | alt | 179 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -9.2) |
| [[KATO III (line)]] | alt | 220 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 122 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.286× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.35× (z +8.7) | — |
| [[NCI-H2030 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -19.2) |
| [[NCI-H23 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -15.3) |
| [[RKO (line)]] | wt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.7) |
| [[SHP-77 (line)]] | alt | 94.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -10.0) |
| [[SNU-423 (line)]] | alt | 74.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.9) |
| [[SW 1088 (line)]] | alt | 193 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0558× (z -13.1) |
| [[SW1417 (line)]] | alt | 166 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -11.5) |
| [[SW48 (line)]] | wt | 153 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.8) |
| [[AN3 CA (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 78.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 89.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 156 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 658), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF4]] | +0.84 | +0.85 / +0.84 | both halves | 7e-06 | STRING 735 |
| [[COPG1]] | +0.82 | +0.83 / +0.83 | both halves | 7e-06 | STRING 528 |
| [[TMEM39A]] | +0.81 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[HYOU1]] | +0.80 | +0.82 / +0.76 | both halves | 7e-06 | STRING 806 |
| [[SEC13]] | +0.80 | +0.84 / +0.77 | both halves | 7e-06 | STRING 682 |
| [[COPA]] | +0.80 | +0.85 / +0.76 | both halves | 7e-06 | STRING 412 |
| [[SEC24D]] | +0.79 | +0.85 / +0.76 | both halves | 7e-06 | STRING 487 |
| [[SSR1]] | +0.78 | +0.75 / +0.74 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 987 |
| [[SEC22B]] | +0.78 | +0.80 / +0.74 | both halves | 7e-06 | pathway: Antigen processing-Cross presentation; STRING 564 |
| [[OSTC]] | +0.77 | +0.82 / +0.72 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 934 |
| [[P4HB]] | +0.77 | +0.78 / +0.80 | both halves | 7e-06 | STRING 855 |
| [[PDIA4]] | +0.77 | +0.83 / +0.71 | both halves | 7e-06 | STRING 681 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT3]] | B | GALNT3 activity raises SEC61A1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.28× lower at baseline in the lines without GALNT3 | 0.077 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.895). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -31.1); signed map (-53.2, 7.7). **Vector** length 150, 53.1% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.71 to 11); *Asparagine N-linked glycosylation* (reactome, mean cos +0.55 to 23); *Maturation of DENV proteins* (reactome, mean cos +0.67 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.3 | +7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.2 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.9 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.8 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.5 | -0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.4 | +3.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +4.0 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.8 | +3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.7 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -11.1 | -13.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.8 | -18.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.7 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.8 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -8.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.5 | -4.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.4 | -3.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.2 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | SEC61 translocon subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:128,051,641-128,071,705 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Sec61 complex subunits |
| Hallmark sets | DNA_REPAIR, P53_PATHWAY |
| Reactome | 6 pathways, smallest: ER-Phagosome pathway; Antigen processing-Cross presentation; Cotranslational targeting of proteins to the endoplasmic reticulum |
| Matched by | ensembl_id |

**Function**, from UniProt [P61619](https://www.uniprot.org/uniprotkb/P61619) (Protein transport protein Sec61 subunit alpha isoform 1):

> Component of SEC61 channel-forming translocon complex that mediates transport of signal peptide-containing precursor polypeptides across the endoplasmic reticulum (ER). Forms a ribosome receptor and a gated pore in the ER membrane, both functions required for cotranslational translocation of nascent polypeptides. May cooperate with auxiliary protein SEC62, SEC63 and HSPA5/BiP to enable post-translational transport of small presecretory proteins. The SEC61 channel is also involved in ER membrane …

**Summary**, from NCBI Gene [29927](https://www.ncbi.nlm.nih.gov/gene/29927):

> The protein encoded by this gene belongs to the SECY/SEC61- alpha family. It appears to play a crucial role in the insertion of secretory and membrane polypeptides into the endoplasmic reticulum. This protein found to be tightly associated with membrane-bound ribosomes, either directly or through adaptor proteins. This gene encodes an alpha subunit of the heteromeric SEC61 complex, which also contains beta and gamma subunits. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18276) · Entrez [29927](https://www.ncbi.nlm.nih.gov/gene/29927) · UniProt [P61619](https://www.uniprot.org/uniprotkb/P61619) · Ensembl [ENSG00000058262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058262)

## Data

Gene col 658: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 658); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 658, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 658]; `tensor/DDL_lfc|DDL_z.npy` [658]; `embed/gene_vectors.npy` [658]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 658 or target_col == 658). Every well: [[SEC61A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC61A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
