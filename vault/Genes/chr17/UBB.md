---
symbol: "UBB"
type: "gene"
col: 9934
ensembl_id: "ENSG00000170315"
name: "ubiquitin B"
location: "17p11.2"
module: 60
arm: "+"
pooled_cpm: 104.99
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# UBB

*ubiquitin B* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (15 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 3.80× (z +11.4, q 2e-27, up in 45 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOD1]] (+0.74, fdr 7e-06), [[DNAJA1]] (+0.69, fdr 7e-06), [[HSPA1A]] (+0.67, fdr 1e-05); moves opposite to [[POFUT1]] (-0.57, fdr 3e-05), [[RMDN3]] (-0.56, fdr 2e-05), [[UBE2G2]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.80×** | +11.4 | 2e-27 | 45/46 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.71×** | +11.2 | 1e-26 | 46/46 (KATO III, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.50×** | +10.1 | 9e-22 | 46/46 (KATO III, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.15×** | +9.8 | 1e-20 | 46/46 (BT-474, C32, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +8.5 | 3e-15 | 45/47 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **6.83×** | +8.1 | 4e-14 | 43/43 (KATO III, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.62×** | +5.8 | 7e-07 | 33/46 (AsPC-1, C32, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.84×** | +5.2 | 1e-05 | 36/47 (NCI-H1792, PANC-1, …) | two highest doses | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.85×** | +5.0 | 3e-05 | 37/46 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.71×** | +4.6 | 2e-04 | 40/46 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **1.73×** | +4.5 | 3e-04 | 32/42 (NCI-H1573, SK-MEL-2, …) | two highest doses | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **1.71×** | +4.4 | 5e-04 | 34/45 (SHP-77, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.61×** | +4.1 | 0.002 | 36/46 (A549, HT-29, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.9 | 0.004 | 36/45 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.59×** | +3.8 | 0.006 | 38/48 (HT-29, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.44×** | +3.5 | 0.013 | 35/47 (KATO III, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.024 | 36/46 (NCI-H2347, BT-474, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.069 | 27/46 (HT-29, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9934.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Budesonide (drug)]] 5 µM |  | 0.703× | -3.0 | 0.74 | 29/46 (hTERT-HPNE, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 199 | 6 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.05× (z +16.2) | — |
| [[A549 (line)]] | wt | 133 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.57× (z +11.4) | — |
| [[C32 (line)]] | wt | 68.6 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 15.8× (z +15.7) | — |
| [[CFPAC-1 (line)]] | alt | 84.6 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.37× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 189 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.80× (z +12.7) ⚠ toxic; cell-cycle shift, explains ~50% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.69× (z +9.8) | — |
| [[SW1417 (line)]] | alt | 120 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.46× (z +14.5) | — |
| [[A-172 (line)]] | wt | 99.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.58× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 130 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.44× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 75.6 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.52× (z +12.6) | — |
| [[hTERT-HPNE (line)]] | wt | 124 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.77× (z +9.5) | — |
| [[LoVo (line)]] | wt | 127 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.19× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 63.3 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.25× (z +10.6) | — |
| [[RKO (line)]] | wt | 93.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 7.11× (z +12.7) | — |
| [[SW480 (line)]] | alt | 162 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.83× (z +11.6) | — |
| [[A498 (line)]] | wt | 138 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.39× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 96.1 | 3 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +17.3) | — |
| [[HS-578T (line)]] | alt | 106 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.55× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 81.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.21× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 113 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.20× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 105 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +12.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.43× (z +9.7) | — |
| [[J82 (line)]] | alt | 118 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.99× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 150 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.91× (z +9.6) | — |
| [[NCI-H460 (line)]] | wt | 97.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.07× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 88.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.47× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 90.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +9.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.47× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 74.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.06× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 85.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.95× (z +9.4) | — |
| [[A-427 (line)]] | wt | 107 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.41× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 106 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 43.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.55× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | — |
| [[NCI-H1792 (line)]] | alt | 41.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-423 (line)]] | alt | 118 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.44× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 102 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.33× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 88.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 91.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 80.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 70.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOD1]] | +0.74 | +0.75 / +0.75 | both halves | 7e-06 | pathway: Cellular response to chemical stress |
| [[DNAJA1]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[HSPA1A]] | +0.67 | +0.52 / +0.74 | both halves | 1e-05 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA; STRING 669 |
| [[PSMB4]] | +0.66 | +0.57 / +0.71 | both halves | 9e-06 | pathway: ABC transporter disorders; STRING 957 |
| [[BAG3]] | +0.65 | +0.54 / +0.66 | both halves | 1e-05 | pathway: Cellular response to heat stress |
| [[HSPB1]] | +0.65 | +0.63 / +0.65 | both halves | 7e-06 | pathway: AUF1 (hnRNP D0) binds and destabilizes mRNA; STRING 772 |
| [[HSP90AB2P]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[HSPA1B]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[HSP90AB3P]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[DEDD2]] | +0.61 | +0.42 / +0.64 | both halves | 4e-05 | pathway: Attenuation phase |
| [[PSMB6]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 | pathway: ABC transporter disorders; STRING 947 |
| [[HSP90AA2P]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POFUT1]] | -0.57 | -0.45 / -0.53 | both halves | 3e-05 | pathway: Signaling by NOTCH |
| [[RMDN3]] | -0.56 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[UBE2G2]] | -0.56 | -0.45 / -0.60 | both halves | 3e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 689 |
| [[FAM120A]] | -0.55 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[QSOX2]] | -0.54 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[ENTR1]] | -0.53 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[CAD]] | -0.52 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[ENTPD5]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[MTG1]] | -0.50 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[TRAP1]] | -0.50 | -0.37 / -0.54 | both halves | 7e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[TXNL4A]] | -0.48 | -0.57 / -0.42 | both halves | 4e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ARL6IP6]] | -0.47 | -0.39 / -0.48 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-18.1, -10.4); signed map (-24.4, -27.4). **Vector** length 109, 46.7% of its response variance represented; |z| ≥ 3 in 842 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.51 to 13); *Mitochondrial unfolded protein response (UPRmt)* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.9 | +10.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.2 | +11.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +11.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.5 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +9.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | +1.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | -6.7 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | -6.3 | +4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.5 | -2.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.2 | -1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:16,380,798-16,382,745 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC8385, FLJ25987 |
| Gene groups (HGNC) | Ubiquitins |
| Reactome | 420 pathways, smallest: Maturation of protein E_9683683; Maturation of protein E_9694493; FLT3 signaling by CBL mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P0CG47](https://www.uniprot.org/uniprotkb/P0CG47) (Polyubiquitin-B):

> [Ubiquitin]: Exists either covalently attached to another protein, or free (unanchored). When covalently bound, it is conjugated to target proteins via an isopeptide bond either as a monomer (monoubiquitin), a polymer linked via different Lys residues of the ubiquitin (polyubiquitin chains) or a linear polymer linked via the initiator Met of the ubiquitin (linear polyubiquitin chains). Polyubiquitin chains, when attached to a target protein, have different functions depending on the Lys residue …

**Summary**, from NCBI Gene [7314](https://www.ncbi.nlm.nih.gov/gene/7314):

> This gene encodes ubiquitin, one of the most conserved proteins known. Ubiquitin has a major role in targeting cellular proteins for degradation by the 26S proteosome. It is also involved in the maintenance of chromatin structure, the regulation of gene expression, and the stress response. Ubiquitin is synthesized as a precursor protein consisting of either polyubiquitin chains or a single ubiquitin moiety fused to an unrelated protein. This gene consists of three direct repeats of the …

**Accessions** — [HGNC:12463](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12463) · Entrez [7314](https://www.ncbi.nlm.nih.gov/gene/7314) · UniProt [P0CG47](https://www.uniprot.org/uniprotkb/P0CG47) · Ensembl [ENSG00000170315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170315)

## Data

Gene col 9934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9934); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9934]; `tensor/DDL_lfc|DDL_z.npy` [9934]; `embed/gene_vectors.npy` [9934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9934 or target_col == 9934). Every well: [[UBB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
