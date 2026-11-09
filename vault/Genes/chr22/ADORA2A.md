---
symbol: "ADORA2A"
type: "gene"
col: 4868
ensembl_id: "ENSG00000128271"
name: "adenosine A2a receptor"
location: "22q11.23"
module: 14
arm: "+"
pooled_cpm: 5.5
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ADORA2A

*adenosine A2a receptor* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.72× (z +10.2, q 8e-22, up in 23 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.547× (z -6.2, q 3e-07, down in 21 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF1]] (+0.70, fdr 7e-06), [[RASSF5]] (+0.65, fdr 7e-06), [[GATM]] (+0.64, fdr 1e-05); moves opposite to [[GFM2]] (-0.47, fdr 1e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[C15orf48]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.72×** | +10.2 | 8e-22 | 23/36 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.61×** | +9.4 | 1e-18 | 26/42 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +8.7 | 8e-16 | 19/37 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.73×** | +5.6 | 3e-06 | 19/43 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.4 | 6e-06 | 12/24 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.8 | 2e-04 | 16/30 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.54×** | +4.4 | 1e-03 | 16/41 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +3.2 | 0.083 | 6/45 (SW480, J82, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.2 | 0.083 | 10/23 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.38× | +3.0 | 0.15 | 7/31 (SNU-423, BT-474, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.547×** | -6.2 | 3e-07 | 21/43 (KATO III, LoVo, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.680×** | -4.0 | 0.021 | 15/43 (NCI-H1573, BT-474, …) | all doses, flat |  |
| [[Thymol (drug)]] 0.05 µM |  | **0.704×** | -3.6 | 0.058 | 10/40 (RKO, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **0.791×** | -3.4 | 0.067 | 9/44 (HepG2/C3A, A-427, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.671×** | -3.4 | 0.067 | 8/43 (NCI-H460, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.704×** | -3.3 | 0.067 | 13/37 (NCI-H2030, LoVo, …) | all doses, flat | position effect removed |
| [[Trimetrexate (drug)]] 5 µM |  | **0.795×** | -3.3 | 0.067 | 6/44 (hTERT-HPNE, J82, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.726×** | -3.3 | 0.067 | 9/45 (hTERT-HPNE, NCI-H1573, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.718×** | -3.3 | 0.067 | 12/43 (NCI-H1573, A549, …) | all doses, flat | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.729×** | -3.2 | 0.067 | 11/39 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | 0.704× | -3.0 | 0.14 | 13/43 (NCI-H1573, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 28.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 8.18× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 11.5 | 0 | 3 (1 ⚠) | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.105× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 4.47 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.14× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.0746× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 3.91 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 23.8× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 4.24 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.4× (z +15.3) | — |
| [[HS-578T (line)]] | alt | 16.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 6.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 4.17 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +12.9) | — |
| [[HOP62 (line)]] | alt | 3.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +8.9) | — |
| [[LoVo (line)]] | wt | 4.19 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0700× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 10.3 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.143× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 5.16 | 0 | 1 | — | [[Penfluridol (drug)]] 0.05 µM 0.0710× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 2.67 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0809× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 5.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 4.21 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 24.5× (z +8.7) | — |
| [[A-172 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF1]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[RASSF5]] | +0.65 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[GATM]] | +0.64 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[NINJ1]] | +0.63 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CSF2]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[SLC2A6]] | +0.63 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.63 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[NKX3-1]] | +0.63 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[LINC02605]] | +0.60 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[SERPINB7]] | +0.60 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[TNFRSF9]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 | STRING 433 |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFM2]] | -0.47 | -0.33 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C15orf48]] | B | C15orf48 activity raises ADORA2A's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.64× lower at baseline in the lines without C15orf48 | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[DRAM1]] | B | DRAM1 activity raises ADORA2A's level | lines that do not express DRAM1 (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without DRAM1 | 0.037 | ⚠ within organs, on part of the lines; also absent: IRX3, ADORA1, BEX3; maybe low, not absent |
| [[OGFRL1]] | B | OGFRL1 activity raises ADORA2A's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without OGFRL1 | 0.045 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[NKX3-1]] | B | NKX3-1 activity raises ADORA2A's level | lines that do not express NKX3-1 (13) vs lines expressing it (37) | 1.65× lower at baseline in the lines without NKX3-1 | 0.066 | ⚠ within organs, on part of the lines; also absent: OSMR, IL1R1, OSMR-DT; maybe low, not absent |
| [[MIR155HG]] | B | MIR155HG activity strengthens ADORA2A's drug response | lines that do not express MIR155HG (26) vs lines expressing it (19) | the lines without MIR155HG respond 0.48× as strongly (z diff +1.02); strongest at Homoharringtonine 5 µM: 1.32x vs 2.96x (z diff +4.0) | 0.069 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA; target measured in part of the lines; artifact flags |
| [[TRAF1]] | B | TRAF1 activity raises ADORA2A's level | lines that do not express TRAF1 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without TRAF1 | 0.072 | ⚠ within organs, on part of the lines; also absent: MT2A, TUBA1A, ENSG00000230479; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ADORA2A's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.661). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.4, 2.9); signed map (41.9, 10.4). **Vector** length 75.8, 13.1% of its response variance represented; |z| ≥ 3 in 1,082 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Chemokine receptors bind chemokines* (reactome, mean cos +0.52 to 8); *Interleukin-10 signaling* (reactome, mean cos +0.52 to 9); *Peptide ligand-binding receptors* (reactome, mean cos +0.51 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.7 | +5.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.3 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.2 | +2.6 |
|  | [[Ivermectin (drug)]] 5 µM |  | +1.1 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.3 | -6.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.2 | -2.2 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.8 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | adenosine A2a receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.23 — chr22:24,417,879-24,442,357 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RDC8; previously ADORA2 |
| Gene groups (HGNC) | Adenosine receptors |
| Reactome | 13 pathways, smallest: Adenosine P1 receptors; NGF-independant TRKA activation; Activation of TRKA receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P29274](https://www.uniprot.org/uniprotkb/P29274) (Adenosine receptor A2a):

> Receptor for adenosine (By similarity). The activity of this receptor is mediated by G proteins which activate adenylyl cyclase (By similarity).

**Summary**, from NCBI Gene [135](https://www.ncbi.nlm.nih.gov/gene/135):

> This gene encodes a member of the guanine nucleotide-binding protein (G protein)-coupled receptor (GPCR) superfamily, which is subdivided into classes and subtypes. The receptors are seven-pass transmembrane proteins that respond to extracellular cues and activate intracellular signal transduction pathways. This protein, an adenosine receptor of A2A subtype, uses adenosine as the preferred endogenous agonist and preferentially interacts with the G(s) and G(olf) family of G proteins to increase …

**Accessions** — [HGNC:263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:263) · Entrez [135](https://www.ncbi.nlm.nih.gov/gene/135) · UniProt [P29274](https://www.uniprot.org/uniprotkb/P29274) · Ensembl [ENSG00000128271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128271)

## Data

Gene col 4868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4868); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4868]; `tensor/DDL_lfc|DDL_z.npy` [4868]; `embed/gene_vectors.npy` [4868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4868 or target_col == 4868). Every well: [[ADORA2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADORA2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
