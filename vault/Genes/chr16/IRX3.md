---
symbol: "IRX3"
type: "gene"
col: 10830
ensembl_id: "ENSG00000177508"
name: "iroquois homeobox 3"
location: "16q12.2"
module: 113
arm: "+"
pooled_cpm: 7.22
n_lines_expressing: 41
n_dd_up: 13
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# IRX3

*iroquois homeobox 3* — 16q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.51× (z +5.0, q 3e-04, up in 17 of 35 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 1.69× (z +4.5, q 0.002, up in 17 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.349× (z -4.7, q 0.001, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1E]] (+0.75, fdr 7e-06), [[MT1M]] (+0.72, fdr 7e-06), [[FOXC2]] (+0.72, fdr 7e-06); moves opposite to [[BPNT2]] (-0.50, fdr 3e-05), [[SIRLNT]] (-0.49, fdr 6e-05), [[AP3M1]] (-0.49, fdr 4e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ITGA10]] → it (grade B ⚠); 4 go from it, the strongest it → [[FZD7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10830.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.51×** | +5.0 | 3e-04 | 17/35 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.69×** | +4.5 | 0.002 | 17/36 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.64×** | +4.2 | 0.004 | 18/36 (NCI-H1792, SW 900, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.014 | 17/33 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.014 | 14/38 (NCI-H1792, SW 900, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.55×** | +3.8 | 0.016 | 16/36 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.57×** | +3.7 | 0.016 | 18/36 (NCI-H1792, HOP62, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.042 | 12/35 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.042 | 13/36 (NCI-H1792, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.4 | 0.042 | 10/28 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.47×** | +3.3 | 0.047 | 13/36 (NCI-H1792, SW 900, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.45×** | +3.2 | 0.062 | 9/29 (HOP62, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.46×** | +3.1 | 0.076 | 15/36 (A498, PANC-1, …) | inconsistent across doses | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10830.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.349×** | -4.7 | 0.001 | 22/36 (HS-578T, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.601×** | -4.4 | 0.003 | 20/37 (HS-578T, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.608×** | -4.0 | 0.010 | 17/36 (SW 900, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.437×** | -3.7 | 0.028 | 15/32 (HOP62, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.653×** | -3.7 | 0.028 | 16/39 (HCT15, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -3.6 | 0.028 | 17/36 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -3.4 | 0.047 | 11/36 (LOX-IMVI, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10830. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 23.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +11.8) ⚠ cell-cycle shift, explains ~63% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 2 | — | [[Cobimetinib (drug)]] 5 µM 0.0639× (z -11.7) |
| [[A549 (line)]] | wt | 5.53 | 0 | 1 | — | [[Fluvoxamine (drug)]] 5 µM 0.0719× (z -9.0) |
| [[C32 (line)]] | wt | 4.46 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.0592× (z -8.8) |
| [[H4 (line)]] | wt | 9.66 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.5 µM 0.0686× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -10.4) ⚠ cell-cycle shift, explains ~14% of this change |
| [[HOP62 (line)]] | alt | 8.17 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +8.7) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0261× (z -15.0) |
| [[A-172 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.585 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10830), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1E]] | +0.75 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[MT1M]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[FOXC2]] | +0.72 | +0.62 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[KLF9]] | +0.72 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CEBPB]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ZFP36L1]] | +0.69 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[ZMYND8]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[ARRDC2]] | +0.67 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[MT2A]] | +0.66 | +0.61 / +0.77 | both halves | 7e-06 |  |
| [[MT1F]] | +0.65 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[MAFB]] | +0.64 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[TLR2]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BPNT2]] | -0.50 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[SIRLNT]] | -0.49 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[AP3M1]] | -0.49 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[TMEM30A]] | -0.49 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[STMP1]] | -0.48 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[PABIR2]] | -0.48 | -0.38 / -0.50 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA10]] | B | ITGA10 activity raises IRX3's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 2.39× lower at baseline in the lines without ITGA10 | 0.074 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises IRX3's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[EBI3]] | C | EBI3 activity raises IRX3's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 2.86× lower at baseline in the lines without EBI3 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FZD7]] | B | IRX3 activity raises FZD7's level | lines that do not express IRX3 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without IRX3 | 0.018 | ⚠ within organs, on part of the lines; also absent: DYSF, DRAM1, LINC02609 |
| [[TK2]] | B | IRX3 activity raises TK2's level | lines that do not express IRX3 (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without IRX3 | 0.036 | ⚠ within organs, on part of the lines; also absent: DYSF, DRAM1, LINC02609 |
| [[TLR2]] | B | IRX3 activity raises TLR2's level | lines that do not express IRX3 (9) vs lines expressing it (41) | 2.88× lower at baseline in the lines without IRX3 | 0.088 | ⚠ within organs, on part of the lines; also absent: DYSF, DRAM1, LINC02609 |
| [[REST]] | B | IRX3 activity raises REST's level | lines that do not express IRX3 (9) vs lines expressing it (41) | 1.60× lower at baseline in the lines without IRX3 | 0.098 | ⚠ within organs, on part of the lines; also absent: DYSF, DRAM1, LINC02609 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.8, 14.1); signed map (15.6, 30.8). **Vector** length 76.8, 17.5% of its response variance represented; |z| ≥ 3 in 719 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.65 to 5); *metallothionein* (control, mean cos +0.65 to 5); *Response to metal ions* (reactome, mean cos +0.65 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.2 | +5.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.6 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.5 | +4.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.4 | +4.2 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.3 | +3.3 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.2 | +2.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | -5.1 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.0 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | -1.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.2 | -0.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.2 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Folic acid (drug)]] 5 µM |  | -1.2 | -2.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.1 | -0.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | iroquois homeobox 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q12.2 — chr16:54,283,304-54,286,787 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IRX-1 |
| Gene groups (HGNC) | TALE class homeoboxes and pseudogenes |
| Matched by | ensembl_id |

**Function**, from UniProt [P78415](https://www.uniprot.org/uniprotkb/P78415) (Iroquois-class homeodomain protein IRX-3):

> Transcription factor involved in SHH-dependent neural patterning. Together with NKX2-2 and NKX6-1 acts to restrict the generation of motor neurons to the appropriate region of the neural tube. Belongs to the class I proteins of neuronal progenitor factors, which are repressed by SHH signals. Involved in the transcriptional repression of MNX1 in non-motor neuron cells. Acts as a regulator of energy metabolism.

**Summary**, from NCBI Gene [79191](https://www.ncbi.nlm.nih.gov/gene/79191):

> IRX3 is a member of the Iroquois homeobox gene family (see IRX1; MIM 606197) and plays a role in an early step of neural development (Bellefroid et al., 1998 [PubMed 9427753]). Members of this family appear to play multiple roles during pattern formation of vertebrate embryos (Lewis et al., 1999 [PubMed 10370142]).[supplied by OMIM, Aug 2009]

**Accessions** — [HGNC:14360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14360) · Entrez [79191](https://www.ncbi.nlm.nih.gov/gene/79191) · UniProt [P78415](https://www.uniprot.org/uniprotkb/P78415) · Ensembl [ENSG00000177508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177508)

## Data

Gene col 10830: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10830); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10830, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10830]; `tensor/DDL_lfc|DDL_z.npy` [10830]; `embed/gene_vectors.npy` [10830]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10830 or target_col == 10830). Every well: [[IRX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
